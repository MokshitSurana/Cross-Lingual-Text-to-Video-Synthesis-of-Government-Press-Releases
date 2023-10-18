'use client'
import React, { useState, useEffect, FormEvent } from 'react'
import useMainContext from '../../context/MainContext'
import MakeVideo from '../../components/MakeVideo'
import ViewScript from '../../components/ViewScript'
import { useRouter } from 'next/navigation'
import toast from 'react-hot-toast'
import { Text } from '../../components'
import { TextAlign } from '../../shared/enums'
import { RxCross2 } from 'react-icons/rx'
import data from "../vaibhav/data.json";
import ModalImage from "../../components/ModalImage";
import { motion } from 'framer-motion';
import { io } from 'socket.io-client'

type Props = {}

const VideoMaker = (props: Props) => {

    const [modal, setModal] = useState(false);
    const [fromPool, setFromPool] = useState(false);
    const [fromCustom, setFromCustom] = useState(false);

    const { selectedArtical, script, setScript, languages, setLanguages }: any = useMainContext();

    const [newScript, setNewScript] = useState("");
    const [isEditing, setIsEditing] = useState(false);
    const [languageModal, setLanguageModal] = useState(false);


    const router = useRouter();

    const fetchScript = async function () {
        // const res = await axioss.post(Api.getScript(), {
        //     article: selectedArtical.content
        // })
        // const data = await res.data.script;
        const data = `Prime Minister Narendra Modi will launch nine new Vande Bharat Express trains on September 24th. These trains will improve connectivity across eleven states and will connect important religious sites such as Puri, Madurai, and Tirupati. The trains will be the fastest on their routes, saving passengers considerable time. The aim is to boost tourism and provide a world-class experience to passengers. The trains will have advanced safety features and amenities, including Kavach technology. This launch is in line with the Prime Minister's vision of improving connectivity and providing top-notch facilities to rail passengers.
        `
        setTimeout(() => {
            setScript(data);
            setNewScript(data);
        }, 4000)
    }

    const handleSubmit = (e: FormEvent<HTMLFormElement>) => {
        const socket = io("https://socketio.sidd065.repl.co"); // !!! SET THIS TO ApiEndpoints.baseUrl WHEN DEPLOYING
        //const socket = io(ApiEndpoints.baseUrl);
        e.preventDefault();
        const form = e.currentTarget;
        const formData = new FormData(form);
        const languages = formData.getAll("languages");
        console.log(languages);
        if (languages.length == 0) {
            toast.error('Select atleast one language!', {
                style: {
                    fontWeight: '400',
                    color: '#000',
                },
            })
            return;
        }
        setLanguages(languages);
        setLanguageModal(false);
        socket.emit("make videos", { script: script, languages: languages });
        router.push('/video');
    }

    const handleSelectAll = (e : React.ChangeEvent<HTMLInputElement> ) => {
        // check if select all check box is cheked or not and select or deselect all languages
        if (e.target.checked) {
            const allLanguages = document.querySelectorAll<HTMLInputElement>('input[type="checkbox"][name="languages"]');
            allLanguages.forEach((language) => {
                language.checked = true;
            })
        } else {
            const allLanguages = document.querySelectorAll<HTMLInputElement>('input[type="checkbox"][name="languages"]');
            allLanguages.forEach((language) => {
                language.checked = false;
            })
        }
    }

    useEffect(() => {
        fetchScript();
    }, [])

    useEffect(() => {
        if (script !== newScript) {
            setIsEditing(true);
        } else {
            setIsEditing(false);
        }
    }, [newScript])

    return (
        <main className='container py-20 md:py-6 mb-4 md:mb-12'>
            <div className='flex flex-col relative'>
                {
                    selectedArtical && (
                        <button className={`z-[5] absolute self-start flex items-center justify-center rounded-md bg-purple-500 text-white hover px-4 pb-2 shadow-lg hover:shadow-none transition-all mb-3`}
                            onClick={() => {
                                setModal(true)
                            }}
                        >
                            <span className='text-base md:text-xl pt-2 block'>View Article</span>
                        </button>
                    )
                }
                {
                    modal && <ViewScript script={selectedArtical?.content} setModal={setModal} />
                }
                {
                    script === "" ? (
                        <div className='flex flex-col w-full items-center justify-center h-[80dvh]'>
                            {/* <div className="animate-spin rounded-full h-44 w-44 border-t-4 border-b-4 border-purple-500"></div> */}

                            {/* <div className="wave-loading-container">
                            <div className="wave"></div>
                            <div className="wave"></div>
                            <div className="wave"></div>
                            <div className="wave"></div>
                            <div className="wave"></div>
                            <div className="wave"></div>
                            <div className="wave"></div>
                            <div className="wave"></div>
                            <div className="wave"></div>
                            <div className="wave"></div>
                        </div> */}

                            <dotlottie-player
                                src="/lotties/scripting.lottie"
                                autoplay
                                loop
                                style={{ height: '50%', width: '50%' }}
                            />

                            <Text textAlign={TextAlign.CENTER} subtitle className='w-[95%] md:w-[80%]' >
                                Generating your script...
                            </Text>
                        </div>
                    ) : (
                        <div className="mx-auto w-full bg-slate-100 dark:bg-slate-900 flex items-start justify-between rounded-2xl">

                            {
                                languageModal && (
                                    <div className='z-10 fixed top-0 bottom-0 left-0 right-0 bg-slate-800 bg-opacity-70 flex justify-center items-center'>
                                        <div className='w-[90%] bg-slate-50 dark:bg-slate-900 p-2 md:p-6 rounded-xl relative'>
                                            <RxCross2
                                                onClick={() => {
                                                    setLanguageModal(false)
                                                }}
                                                className="text-slate-900 dark:text-white absolute top-2.5 right-2.5 text-3xl cursor-pointer"
                                            />
                                            <Text subtitle className='text-center' >
                                                Select languages
                                            </Text>
                                            <hr />
                                            <form onSubmit={handleSubmit} className='my-[10px] flex flex-col gap-4'>
                                                {/* Select all checkbox to select all languages */}
                                                <div className="flex items-center mr-4">
                                                    <input id="checkbox-0" type="checkbox" className="w-4 h-4 text-purple-600 bg-gray-100 border-gray-300 rounded accent-green-600"
                                                        onChange={handleSelectAll}
                                                    />
                                                    <label htmlFor="checkbox-0" className="ml-2 text-sm font-bold text-gray-900 dark:text-gray-300">All</label>
                                                </div>
                                                {/* Languages */}
                                                <div className='grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4'>
                                                    <div className="flex items-center mr-4">
                                                        <input id="checkbox-1" type="checkbox" name="languages" value="Hindi" className="w-4 h-4 text-purple-600 bg-gray-100 border-gray-300 rounded accent-purple-600" />
                                                        <label htmlFor="checkbox-1" className="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">Hindi</label>
                                                    </div>
                                                    <div className="flex items-center mr-4">
                                                        <input id="checkbox-2" type="checkbox" name="languages" value="English" className="w-4 h-4 text-purple-600 bg-gray-100 border-gray-300 rounded accent-purple-600" />
                                                        <label htmlFor="checkbox-2" className="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">English</label>
                                                    </div>
                                                    <div className="flex items-center mr-4">
                                                        <input id="checkbox-3" type="checkbox" name="languages" value="Marathi" className="w-4 h-4 text-purple-600 bg-gray-100 border-gray-300 rounded accent-purple-600" />
                                                        <label htmlFor="checkbox-3" className="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">Marathi</label>
                                                    </div>
                                                    <div className="flex items-center mr-4">
                                                        <input id="checkbox-4" type="checkbox" name="languages" value="Bengali" className="w-4 h-4 text-purple-600 bg-gray-100 border-gray-300 rounded accent-purple-600" />
                                                        <label htmlFor="checkbox-4" className="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">Bengali</label>
                                                    </div>
                                                    <div className="flex items-center mr-4">
                                                        <input id="checkbox-5" type="checkbox" name="languages" value="Gujarati" className="w-4 h-4 text-purple-600 bg-gray-100 border-gray-300 rounded accent-purple-600" />
                                                        <label htmlFor="checkbox-5" className="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">Gujarati</label>
                                                    </div>
                                                    <div className="flex items-center mr-4">
                                                        <input id="checkbox-6" type="checkbox" name="languages" value="Kannada" className="w-4 h-4 text-purple-600 bg-gray-100 border-gray-300 rounded accent-purple-600" />
                                                        <label htmlFor="checkbox-6" className="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">Kannada</label>
                                                    </div>
                                                    <div className="flex items-center mr-4">
                                                        <input id="checkbox-7" type="checkbox" name="languages" value="Malayalam" className="w-4 h-4 text-purple-600 bg-gray-100 border-gray-300 rounded accent-purple-600" />
                                                        <label htmlFor="checkbox-7" className="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">Malayalam</label>
                                                    </div>
                                                    <div className="flex items-center mr-4">
                                                        <input id="checkbox-8" type="checkbox" name="languages" value="Tamil" className="w-4 h-4 text-purple-600 bg-gray-100 border-gray-300 rounded accent-purple-600" />
                                                        <label htmlFor="checkbox-8" className="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">Tamil</label>
                                                    </div>
                                                    <div className="flex items-center mr-4">
                                                        <input id="checkbox-9" type="checkbox" name="languages" value="Telugu" className="w-4 h-4 text-purple-600 bg-gray-100 border-gray-300 rounded accent-purple-600" />
                                                        <label htmlFor="checkbox-9" className="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">Telugu</label>
                                                    </div>
                                                    <div className="flex items-center mr-4">
                                                        <input id="checkbox-10" type="checkbox" name="languages" value="Urdu" className="w-4 h-4 text-purple-600 bg-gray-100 border-gray-300 rounded accent-purple-600" />
                                                        <label htmlFor="checkbox-10" className="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">Urdu</label>
                                                    </div>
                                                    <div className="flex items-center mr-4">
                                                        <input id="checkbox-11" type="checkbox" name="languages" value="Punjabi" className="w-4 h-4 text-purple-600 bg-gray-100 border-gray-300 rounded accent-purple-600" />
                                                        <label htmlFor="checkbox-11" className="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">Punjabi</label>
                                                    </div>
                                                    <div className="flex items-center mr-4">
                                                        <input id="checkbox-12" type="checkbox" name="languages" value="Odia" className="w-4 h-4 text-purple-600 bg-gray-100 border-gray-300 rounded accent-purple-600" />
                                                        <label htmlFor="checkbox-12" className="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">Odia</label>
                                                    </div>
                                                    <div className="flex items-center mr-4">
                                                        <input id="checkbox-12" type="checkbox" name="languages" value="Assamese" className="w-4 h-4 text-purple-600 bg-gray-100 border-gray-300 rounded accent-purple-600" />
                                                        <label htmlFor="checkbox-12" className="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">Assamese</label>
                                                    </div>
                                                </div>
                                                <button className="bg-purple-500 hover:bg-purple-700 text-white font-bold py-2 px-4 rounded self-start">
                                                    Proceed
                                                </button>
                                            </form>
                                        </div>
                                    </div>
                                )
                            }
                            <div className="w-full scrollbar-hide">
                                <motion.div
                                    className={`flex flex-col gap-2 ${fromCustom || "hidden"}`}
                                    initial="hidden" animate={fromCustom ? "visible" : "hidden"} variants={{
                                        hidden: {
                                            opacity: 0,
                                            x: "100%"
                                        },
                                        visible: {
                                            opacity: 1,
                                            x: "0%",
                                            transition: {
                                                // delay: 0.5
                                            }
                                        }
                                    }}
                                >
                                    <h3 className="text-center font-bold text-3xl my-[10px] text-gray-800 dark:text-white text-md md:text-3xl mt-0 w-full pb-12 sticky top-0 bg-slate-100 dark:bg-slate-900">
                                        Choose appropriate images for the script
                                        {/* <button className={`flex items-center justify-center rounded-md ${isEditing ? "bg-red-500 text-white hover:text-white" : "bg-gray-400 text-gray-900"} text-sm px-3.5 py-1.5 shadow-lg hover:shadow-none transition-all mb-3 absolute bottom-0 right-0`}
                                            disabled={!isEditing}
                                            onClick={() => {
                                                setNewScript(script)
                                            }}
                                        >
                                            <span className='text-base block'>Reset</span>
                                        </button> */}
                                    </h3>
                                    {data.map((item, index) => {
                                        return (
                                            <ModalImage
                                                key={index}
                                                script={item.sentence}
                                                imageList={item.images}
                                                timeStamp={item.timeStamp}
                                            />
                                        );
                                    })}
                                </motion.div>
                                <motion.div
                                    className={`flex flex-col gap-2 ${fromCustom && "hidden"}`}
                                    initial="hidden" animate={fromCustom ? "hidden" : "visible"} variants={{
                                        hidden: {
                                            opacity: 0,
                                            x: "-100%"
                                        },
                                        visible: {
                                            opacity: 1,
                                            x: "0%",
                                            transition: {
                                                // delay: 0.5
                                            }
                                        }
                                    }}
                                >
                                    <Text title textAlign={TextAlign.CENTER} className="text-md md:text-3xl mt-0 w-full pb-12 sticky top-0 bg-slate-100 dark:bg-slate-900">
                                        Generated Script

                                        <button className={`flex items-center justify-center rounded-md ${isEditing ? "bg-red-500 text-white hover:text-white" : "bg-gray-400 text-gray-900"} text-sm px-3.5 py-1.5 shadow-lg hover:shadow-none transition-all mb-3 absolute bottom-0 right-0`}
                                            disabled={!isEditing}
                                            onClick={() => {
                                                setNewScript(script)
                                            }}
                                        >
                                            <span className='text-base block'>Reset</span>
                                        </button>
                                    </Text>
                                    <textarea
                                        value={newScript}
                                        onChange={(e) => {
                                            setNewScript(e.target.value || '')
                                        }}
                                        className={`scrollbar-hide w-full h-[90vh] md:h-[60vh] font-regular mb-3 leading-relaxed text-gray-800 dark:text-white text-sm md:text-xl whitespace-pre-wrap shadow-inset p-4 border border-gray-300 focus:border-purple-500 dark:bg-gray-800 dark:border-gray-600  dark:focus:border-purple-500`}
                                    />
                                </motion.div>
                                <div
                                    className='flex relative'
                                >
                                    <details>
                                        <summary className="relative px-5 py-2 font-medium text-gray-900 dark:text-white group">
                                            Advance Option
                                        </summary>
                                        <div
                                            className='flex flex-col gap-2 px-5 py-2 font-medium text-white group'
                                        >
                                            <div
                                                className='flex flex-col text-gray-900 dark:text-white space-y-2'
                                            >
                                                <div
                                                    className='flex items-center'
                                                >
                                                    <input checked={fromPool} onChange={(e) => setFromPool(e.target.checked)} type="checkbox" className='text-purple-600 bg-gray-100 border-gray-300 rounded accent-purple-600' id="pool" name="pool" />
                                                    <label htmlFor="pool" className='text-gray-900 ml-2'>Select Image Pool</label>
                                                </div>
                                                {
                                                    fromPool && (
                                                        <motion.div
                                                            initial="hidden" animate={fromPool ? "visible" : "hidden"} variants={{
                                                                hidden: {
                                                                    opacity: 0,
                                                                    y: -50
                                                                },
                                                                visible: {
                                                                    opacity: 1,
                                                                    y: 0
                                                                }
                                                            }}
                                                            className="md:flex md:items-center mb-2 ml-3">
                                                            <div className="md:w-1/3">
                                                                <label className="block text-gray-500 md:text-right mb-1 md:mb-0 pr-4" htmlFor="inline-full-name">
                                                                    Select Pool
                                                                </label>
                                                            </div>
                                                            <div className="md:w-2/3">
                                                                <input className="bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500" id="inline-full-name" type="text" placeholder='G20' />
                                                            </div>
                                                        </motion.div>
                                                    )
                                                }

                                            </div>
                                            <div
                                                className='flex items-center'
                                            >
                                                <input type="checkbox" checked={fromCustom} onChange={(e) => setFromCustom(e.target.checked)} className='text-purple-600 bg-gray-100 border-gray-300 rounded accent-purple-600' id="custom" name="custom" />
                                                <label htmlFor="custom" className='text-gray-900 ml-2'>Approve Images</label>
                                                <span
                                                    className='text-xs ml-2 text-gray-400'
                                                >
                                                    (Recommended)
                                                </span>
                                            </div>
                                        </div>
                                    </details>
                                </div>
                                <div
                                    className='flex relative'
                                >
                                    <div
                                        className="absolute right-2"
                                    >
                                        <button
                                            onClick={() => {
                                                isEditing && setScript(newScript);
                                                setLanguageModal(true);
                                            }}
                                            className="relative px-5 py-2 font-medium text-white group">
                                            <span className="absolute inset-0 w-full h-full transition-all duration-300 ease-out transform translate-x-0 -skew-x-12 bg-purple-500 group-hover:bg-purple-700 group-hover:skew-x-12"></span>
                                            <span className="absolute inset-0 w-full h-full transition-all duration-300 ease-out transform skew-x-12 bg-purple-700 group-hover:bg-purple-500 group-hover:-skew-x-12"></span>
                                            <span className="absolute bottom-0 left-0 hidden w-10 h-20 transition-all duration-100 ease-out transform -translate-x-8 translate-y-10 bg-purple-600 -rotate-12"></span>
                                            <span className="absolute bottom-0 right-0 hidden w-10 h-20 transition-all duration-100 ease-out transform translate-x-10 translate-y-8 bg-purple-400 -rotate-12"></span>
                                            <span className="relative text-white text-xl">Make Video</span>
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    )
                }
            </div>
        </main >
    )
}

export default VideoMaker;