'use client'

import React, { useEffect, useState } from 'react'
import { Socket, io } from 'socket.io-client'
import Text from './Text/Text'
import { Languages, TextAlign } from '../shared/enums'
import useMainContext from '../context/MainContext'
import ReactPlayer from 'react-player'
import axioss from '../utils/axiosInterceptor'
import { Api } from '../utils/api.config'
import { BsFillShareFill } from 'react-icons/bs'
import Utube from '../assets/utube.png'
import Insta from '../assets/insta.png'
import FB from '../assets/facebook.png'
import X from '../assets/x.webp'

const ApiEndpoints = {
    baseUrl: process.env.NEXT_PUBLIC_BASE_URL
}

// define a type for VideoType having key as any Language and value as string
type VideoType = {
    [key in typeof Languages[number]['name']]: string
}

const MakeVideo = () => {

    const { script, languages }: any = useMainContext();

    const [videos, setVideos] = useState<VideoType | null>(null);
    const langaugesProgress = languages.reduce((accumulator: String, value: number) => {
        return { ...accumulator, [value]: { step: "Translating Script...", progress: 0 } };
    }, {});
    const [progress, setProgress] = useState<object>(langaugesProgress);
    const socket = io("https://socketio.sidd065.repl.co"); // !!! SET THIS TO ApiEndpoints.baseUrl WHEN DEPLOYING
    //const socket = io(ApiEndpoints.baseUrl);

    // @ts-ignore  
    useEffect(() => {
        socket.on("progress update", (data) => { //{"language":"Hindi","step":"Writing script", "progress":10, "data": '' or videoUrl}

            console.log(data)
            if (data.step == "Video Ready") {
                console.log(data.data, languages.length)
                setVideos({ ...videos, [data.language]: data.data });
                let temp = progress;
                // @ts-ignore
                delete temp[data.language];
                setProgress(temp);
            }
            else if (data.step == "All Videos Ready") {
                console.log('disconnecting socket...')
                socket.disconnect()
            }
            else {
                setProgress({ ...progress, [data.language]: { step: data.step, progress: data.progress } });
            }
        });
        return () => socket.off('progress update');
    });

    // const fetchVideo = async () => {
    //     // const tempScript = "India's President, Srimati Droupadi Murmu, unveiled a 12-foot statue of Mahatma Gandhi in New Delhi. She highlighted Gandhi's ideals, which have guided the world towards non-violence during times of global conflict. She stressed the need for integrity in public and personal life. The President encouraged everyone to learn about Gandhi's teachings through various mediums, to build the India of his dreams. She emphasized making the youth and children more aware of his life teachings."
    //     // const tempLangs = ["English", "Hindi"]

    //     // const res = await axioss.post(Api.getVideo(), {
    //     //     script,
    //     //     languages
    //     // })
    //     // const data = await res.data;
    //     // console.log("Data", data)
    //     // setVideos(data)


    //     setTimeout(() => { // !!! Can be used for static demo
    //         setVideos({
    //             "English": "https://22e7f9ae135c06371b.gradio.live/file=/home/siddharth/ShortGPT/videos/2023-09-11_21-12-05[Language.ENGLISH]-Title.mp4",
    //             "Marathi": "https://22e7f9ae135c06371b.gradio.live/file=/home/siddharth/ShortGPT/videos/2023-09-11_21-11-57[Language.MARATHI]-Title.mp4"
    //         })
    //     }, 5000)
    // }

    // const fetchLaodingDetails = async (socket: Socket) => {
    //     // socket.emit('fetchLoadingDetails', props.selectedArtical)

    //     await fetchVideo();

    //     // socket.on('loadingDetails', (data: any) => {
    //     //     console.log(data)
    //     // })
    // }


    // useEffect(() => {



    //     socket.emit("make videos", {script:script, languages:languages});

    //     // const socket = io(process.env.NEXT_PUBLIC_BASE_URL || "", {
    //     //     transports: ['websocket']
    //     // })
    //     // const socket = "temp" as any;

    //     //fetchLaodingDetails(socket);

    //     // return () => {
    //     //     console.log('disconnecting socket...')
    //     //     // socket.disconnect()
    //     // }
    // }, [])

    return (
        <div
            className="flex flex-col space-y-6 my-4 w-full items-center justify-center"
        >
            {
                videos ? (
                    <>
                        {Object.keys(progress).map((language, i) => (
                            <Text key={i} textAlign={TextAlign.CENTER} subtitle className='w-[95%] md:w-[80%]'>
                                {/* @ts-ignore */}
                                {`${language}: ${progress[language]['step']} - ${progress[language]['progress']}%`}
                            </Text>
                        ))}
                        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6 w-full">
                            {
                                videos && Object.keys(videos).map((key, index) => {
                                    return (
                                        <div
                                            key={index}
                                            className="flex flex-col space-y-2 p-4 rounded-md w-full border-2 border-gray-200 dark:border-slate-800"
                                        >
                                            {/* <div className='flex items-center justify-between'>
                                            
                                            <button
                                                className='bg-purple-600 p-2 rounded-md'
                                            >
                                                <BsFillShareFill className='text-slate-50 text-lg cursor-pointer' />
                                            </button>
                                        </div> */}
                                            <p className='text-gray-800 dark:text-slate-50 font-semibold'>{key}</p>
                                            <div
                                                className="flex p-4 rounded-md relative w-full aspect-[9/16]"
                                            >
                                                <ReactPlayer
                                                    width="100%"
                                                    height="100%"
                                                    style={{
                                                        position: 'absolute',
                                                        top: 0,
                                                        left: 0,
                                                        zIndex: 1,
                                                        border: '1px solid #ccc',
                                                        borderRadius: '4px'
                                                    }}
                                                    controls
                                                    url={videos[key]}
                                                />
                                            </div>
                                            {/* <button
                                            className='bg-purple-600 p-2 font-bold rounded-md text-slate-50'
                                        >
                                            Upload to Youtube
                                        </button>
                                        <button
                                            className='bg-purple-600 p-2 font-bold rounded-md text-slate-50'
                                        >
                                            Upload to Instagram
                                        </button> */}
                                            <div className='flex items-center justify-between gap-2'>
                                                <img src={Utube.src} alt="utube" className='w-10 h-10 border rounded-lg shadow-lg p-2' />
                                                <img src={Insta.src} alt="insta" className='w-10 h-10 border rounded-lg shadow-lg p-2' />
                                                <img src={FB.src} alt="insta" className='w-10 h-10 border rounded-lg shadow-lg p-2' />
                                                <img src={X.src} alt="insta" className='w-10 h-10 border rounded-lg shadow-lg p-2' />
                                            </div>

                                        </div>
                                    )
                                }
                                )
                            }
                        </div></>
                ) : (
                    <>
                        {/* <iframe src="https://lottie.host/?file=4b7dca07-aed2-4856-a909-5ad17ecc8f01/Ux1tTLuFsu.json"></iframe> */}

                        <dotlottie-player
                            src="/lotties/gears.lottie"
                            autoplay
                            loop
                            style={{ height: '30%', width: '30%' }}
                        />
                        {Object.keys(progress).map((language, i) => (
                            <Text key={i} textAlign={TextAlign.CENTER} subtitle className='w-[95%] md:w-[80%]' >
                                {/* @ts-ignore */}
                                {`${language}: ${progress[language]['step']} - ${progress[language]['progress']}%`}
                            </Text>
                        ))}


                    </>
                )
            }
        </div>
    )
}

export default MakeVideo



// {
//     "English": "https://c848d3eaf28410caa3.gradio.live/file=videos/2023-09-10_21-34-30[Language.ENGLISH]-Title.mp4",
//     "Hindi": "https://c848d3eaf28410caa3.gradio.live/file=videos/2023-09-10_21-36-02[Language.HINDI]-Title.mp4"
// }