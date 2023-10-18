'use client'

import React, { useEffect } from 'react'
import { useRouter } from 'next/navigation'
import Text from './Text/Text'
import { TextAlign } from '../shared/enums'
import { RxCross2 } from 'react-icons/rx'
import useMainContext from '../context/MainContext'

type ImageType = {
    file: File | null,
    caption: string
}
const CreatePool = ({
    setCreatePool
}: {
    setCreatePool: React.Dispatch<React.SetStateAction<boolean>>,
}) => {

    const router = useRouter();

    const [images, setImages] = React.useState<ImageType[]>([{
        file: null,
        caption: ""
    }]);
    // const text = `The President of India, Smt Droupadi Murmu  unveiled the 12 feet high statue of Mahatma Gandhi and inaugurated ‘Gandhi Vatika’ at Gandhi Darshan, New Delhi today (September 4, 2023).\n
    // Speaking on the occasion, the President said that Mahatma Gandhi is a boon for the entire world community. His ideals and values have given a new direction to the whole world. He showed the path of non-violence at a time when the world was suffering from many kinds of hatred and discord during the period of world wars. She added that Gandhiji's experiment with truth and non-violence gave him the status of a great human. She shared that his statues are installed in many countries and people from across the world believe in his ideals. Giving examples of Nelson Mandela, Martin Luther King Jr. and Barack Obama, she said that many great leaders considered the path of truth and non-violence shown by Gandhiji as the path of world welfare. She emphasised that by following the path shown by him, the goal of world peace can be achieved.\n
    // The President said that Gandhiji laid great emphasis on sanctity in public as well as in personal life. He believed that violence can be faced through non-violence only on the basis of moral strength. She underlined that without self-confidence, one cannot act with persistence in adverse circumstances. She stated that in today's fast-changing and competitive world, there is great need for self-confidence and temperance.\n
    // The President said that Gandhiji laid great emphasis on sanctity in public as well as in personal life. He believed that violence can be faced through non-violence only on the basis of moral strength. She underlined that without self-confidence, one cannot act with persistence in adverse circumstances. She stated that in today's fast-changing and competitive world, there is great need for self-confidence and temperance.\n
    // The President said that Gandhiji laid great emphasis on sanctity in public as well as in personal life. He believed that violence can be faced through non-violence only on the basis of moral strength. She underlined that without self-confidence, one cannot act with persistence in adverse circumstances. She stated that in today's fast-changing and competitive world, there is great need for self-confidence and temperance.\n
    // The President said that Gandhiji laid great emphasis on sanctity in public as well as in personal life. He believed that violence can be faced through non-violence only on the basis of moral strength. She underlined that without self-confidence, one cannot act with persistence in adverse circumstances. She stated that in today's fast-changing and competitive world, there is great need for self-confidence and temperance.\n
    // The President said that Gandhiji laid great emphasis on sanctity in public as well as in personal life. He believed that violence can be faced through non-violence only on the basis of moral strength. She underlined that without self-confidence, one cannot act with persistence in adverse circumstances. She stated that in today's fast-changing and competitive world, there is great need for self-confidence and temperance.\n
    // The President said that Gandhiji's ideals and values are very relevant for our country and society. She urged all to make efforts so that every citizen, especially the youth and children, read as much as possible about Gandhiji and imbibe his ideals. She said that the role of Gandhi Smriti and Darshan Samiti and other such institutions becomes very important in this regard. She said that they can contribute significantly in building the India of Gandhiji's dreams by making the youth and children more aware of Gandhiji's life teachings through books, films, seminars, cartoons and other media.`

    useEffect(() => {
        console.log(images);
    }, [images])

    return (
        <div
            className="fixed z-20 top-0 bottom-0 left-0 right-0 bg-slate-800 bg-opacity-70 flex justify-center items-center"
        >
            <div className="absolute mx-auto top-8 bottom-8 w-[95%] md:w-[80%] bg-slate-100 dark:bg-slate-900 flex items-start px-3.5 md:px-12 pt-12 pb-28 justify-between h-[90lvh] rounded-2xl">
                <RxCross2
                    onClick={() => setCreatePool(false)}
                    className="text-slate-900 dark:text-white absolute top-2.5 right-2.5 text-3xl cursor-pointer"
                />
                <div className="overflow-y-auto h-full w-full scrollbar-hide">
                    <Text title textAlign={TextAlign.CENTER} className="z-10 text-md md:text-3xl mt-0 w-full pb-4 sticky top-0 bg-slate-100 dark:bg-slate-900">
                        Create New Pool
                    </Text>

                    <form
                        onSubmit={(e) => {
                            e.preventDefault();
                            // setCreatePool(false);
                            // router.push(`/pools/${Math.floor(Math.random() * 100) + 1}`)
                        }}
                        className="flex flex-col gap-4 w-full "
                    >
                        <div className='flex gap-4 items-center'>
                            <label htmlFor="pool-name" className='font-semibold md:text-xl text-gray-700 w-24'>Name</label>
                            <input id="pool-name" className="bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500" type="text" placeholder='G20' />
                        </div>
                        <div className='flex gap-4 items-start'>
                            <label htmlFor="pool-name" className='font-semibold md:text-xl text-gray-700 w-24'>Images</label>
                            <div className="flex items-center w-full gap-6 flex-wrap">
                                {
                                    images.map((image, index) => {
                                        return (
                                            image?.file ? (
                                                <div className="relative p-2 border-2 border-gray-300 rounded-xl"
                                                    key={index}
                                                >
                                                    <div className='w-60 h-60 mb-2 border shadow-sm'>
                                                        <img
                                                            className="w-full h-full object-cover rounded-xl"
                                                            src={URL.createObjectURL(image?.file)}
                                                            alt="Image"
                                                        />
                                                    </div>
                                                    <input className="bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500" type="text" placeholder='Caption' required />
                                                    <button
                                                        className="absolute -top-4 -right-4 w-8 h-8 bg-red-500 rounded-full flex items-center justify-center"
                                                        onClick={(e) => {
                                                            e.preventDefault();
                                                            setImages(prev => prev.filter((_, i) => i !== index))
                                                        }}
                                                    >
                                                        <RxCross2 className="w-4 h-4 text-white" />
                                                    </button>
                                                </div>
                                            ) : (
                                                <label
                                                    key={index}
                                                    htmlFor="dropzone-file"
                                                    className="flex flex-col items-center justify-center border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 hover:bg-gray-100"
                                                >
                                                    <div className="w-60 h-60 flex flex-col items-center justify-center pt-5 pb-6 ">
                                                        <svg
                                                            className="w-10 h-10 mb-3 text-gray-400"
                                                            fill="none"
                                                            stroke="currentColor"
                                                            viewBox="0 0 24 24"
                                                            xmlns="http://www.w3.org/2000/svg"
                                                        >
                                                            <path
                                                                strokeLinecap="round"
                                                                strokeLinejoin="round"
                                                                strokeWidth="2"
                                                                d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
                                                            ></path>
                                                        </svg>
                                                        <p className="mb-2 text-sm text-gray-500">
                                                            <span className="font-semibold">Click to upload</span>
                                                        </p>
                                                        <p className="text-xs text-gray-500">
                                                            SVG, PNG or Webp
                                                        </p>
                                                    </div>
                                                    <input
                                                        onChange={(e) => {
                                                            if (e.target.files) {
                                                                if (images.length === 1) {
                                                                    setImages(prev => [{
                                                                        file: e.target.files && e.target.files[0],
                                                                        caption: ""
                                                                    }, ...prev])
                                                                } else {
                                                                    setImages(prev => {
                                                                        let temp = prev.slice(0, prev.length - 1);
                                                                        return [
                                                                            ...temp,
                                                                            {
                                                                                file: e.target.files ? e.target.files[0] : null,
                                                                                caption: ""
                                                                            },
                                                                            {
                                                                                file: null,
                                                                                caption: ""
                                                                            }
                                                                        ]
                                                                    });
                                                                }
                                                            }
                                                        }}
                                                        id="dropzone-file"
                                                        type="file"
                                                        accept="image/*"
                                                        className="hidden"
                                                    />
                                                </label>
                                            )
                                        )
                                    })
                                }
                            </div>
                        </div>

                        <div
                            className="absolute bottom-7 right-7"
                        >
                            <button
                                type='submit'
                                className="relative px-5 py-2 font-medium text-white group">
                                <span className="absolute inset-0 w-full h-full transition-all duration-300 ease-out transform translate-x-0 -skew-x-12 bg-purple-500 group-hover:bg-purple-700 group-hover:skew-x-12"></span>
                                <span className="absolute inset-0 w-full h-full transition-all duration-300 ease-out transform skew-x-12 bg-purple-700 group-hover:bg-purple-500 group-hover:-skew-x-12"></span>
                                <span className="absolute bottom-0 left-0 hidden w-10 h-20 transition-all duration-100 ease-out transform -translate-x-8 translate-y-10 bg-purple-600 -rotate-12"></span>
                                <span className="absolute bottom-0 right-0 hidden w-10 h-20 transition-all duration-100 ease-out transform translate-x-10 translate-y-8 bg-purple-400 -rotate-12"></span>
                                <span className="relative text-white text-xl">Create Pool</span>
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    )
}

export default CreatePool