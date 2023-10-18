'use client'

import React, { FormEvent, FormEventHandler, useEffect, useState } from 'react'
import { Socket, io } from 'socket.io-client'
import { iArticle } from '../shared/interfaces'
import Text from './Text/Text'
import { TextAlign } from '../shared/enums'
import { RxCross2 } from 'react-icons/rx'
import { useRouter } from 'next/navigation'
import useMainContext from '../context/MainContext'
import axioss from '../utils/axiosInterceptor'
import { Api } from '../utils/api.config'
import toast from 'react-hot-toast'

const MakeScript = () => {

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
        const data = `This is a sample script. Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, voluptatum.        Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, voluptatum. Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, voluptatum.   Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, voluptatum.
        `
        setTimeout(() => {
            setScript(data);
            setNewScript(data);
        }, 4000)
    }

    console.log("languages", script)

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

    useEffect(() => {
        fetchScript();
    }, [])

    useEffect(() => {
        if (script !== newScript) {
            setIsEditing(true);
        } else {
            setIsEditing(false);
        }
        console.log("script", newScript)
    }, [newScript])

    return (
        <div
            className="fixed z-20 top-0 bottom-0 left-0 right-0 bg-slate-800 bg-opacity-70 flex justify-center items-center flex-col gap-6"
        >
            {
                script === "" ? (
                    <>
                        <dotlottie-player
                            src="/lotties/scripting.lottie"
                            autoplay
                            loop
                            style={{ height: '50%', width: '50%' }}
                        />

                        <Text color='white' textAlign={TextAlign.CENTER} subtitle className='w-[95%] md:w-[80%]' >
                            Generating your script...
                        </Text>
                    </>
                ) : (
                    <div
                        className="fixed z-20 top-0 bottom-0 left-0 right-0 bg-slate-800 bg-opacity-70 flex justify-center items-center"
                    >
                        <div className="absolute mx-auto top-8 bottom-8 w-[95%] md:w-[80%] bg-slate-100 dark:bg-slate-900 flex items-start px-3.5 md:px-12 pt-12 pb-28 justify-between h-[90lvh] rounded-2xl">

                            {
                                languageModal && (
                                    <div className='z-10 absolute top-0 bottom-0 left-0 right-0 bg-slate-800 bg-opacity-70 flex justify-center items-center'>
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
                                            <form
                                                onSubmit={handleSubmit}
                                                className='my-[10px] flex flex-col gap-4'>
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
                                                        <input id="checkbox-13" type="checkbox" name="languages" value="Assamese" className="w-4 h-4 text-purple-600 bg-gray-100 border-gray-300 rounded accent-purple-600" />
                                                        <label htmlFor="checkbox-13" className="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">Assamese</label>
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
                            <RxCross2
                                onClick={() => {
                                    setScript("")
                                }}
                                className="text-slate-900 dark:text-white absolute top-2.5 right-2.5 text-3xl cursor-pointer"
                            />
                            <div
                                className="absolute bottom-7"
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
                            <div className="overflow-y-auto h-full w-full scrollbar-hide">
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
                                    className={`scrollbar-hide w-full h-full font-regular mb-3 leading-relaxed text-gray-800 dark:text-white text-sm md:text-xl whitespace-pre-wrap shadow-inset p-4 border border-gray-300 focus:border-purple-500 dark:bg-gray-800 dark:border-gray-600  dark:focus:border-purple-500`} />
                            </div>
                        </div>
                    </div>
                )
            }
        </div>
    )
}

export default MakeScript