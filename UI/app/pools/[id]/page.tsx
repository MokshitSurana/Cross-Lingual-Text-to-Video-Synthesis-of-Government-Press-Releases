'use client'
import React, { useState, useEffect, FormEvent } from 'react'
import { BsPlus } from 'react-icons/bs';
import { Text } from '../../../components';
import Temp from '../../../assets/bg.png';
import Link from 'next/link';
import CreatePool from '../../../components/CreatePool';

type Props = {}

const Pools = (props: Props) => {

    const [pools, setPools] = useState<any[]>([]);
    const [createPool, setCreatePool] = useState<boolean>(false);

    const fetchScript = async function () {
        // const res = await axioss.post(Api.getScript(), {
        //     article: selectedArtical.content
        // })
        // const data = await res.data.script;
        const data = [
            {
                id: 1,
                name: 'Pool 1',
                description: 'This is pool 1',
                images: [
                    {
                        source: "",
                        caption: ""
                    },
                    {
                        source: "",
                        caption: ""
                    }
                ]
            },
            {
                id: 2,
                name: 'Pool 2',
                description: 'This is pool 2',
                images: [
                    {
                        source: "",
                        caption: ""
                    },
                    {
                        source: "",
                        caption: ""
                    }
                ]
            }
        ]
        setTimeout(() => {
            setPools(data);
        }, 4000)
    }

    useEffect(() => {
        fetchScript();
    }, [])

    return (
        <main className='container py-20 md:py-6 mb-4 md:mb-12'>
            {
                createPool && (
                    <CreatePool setCreatePool={setCreatePool} />
                )
            }
            <div className='flex flex-col'>
                <div
                    className='flex items-center justify-between w-full'
                >
                    <Text title>
                        Pools
                    </Text>
                    <button
                        onClick={() => { 
                            setCreatePool(true)
                        }}
                        className='px-2 md:px-4 py-2 rounded-md bg-purple-500 flex items-center justify-center gap-1'
                    >
                        <BsPlus className='w-6 h-6 text-white' />
                        <span className='hidden md:block text-white font-semibold'>Add Pool</span>
                    </button>
                </div>
                <hr className="h-px my-4 bg-gray-200 border-0 dark:bg-gray-700" />
                <div className='grid gap-4 grid-cols-1 sm:grid-cols-2 md:grid-cols-4'>
                    {
                        Array(10).fill(0).map((pool, index) => {
                            return (
                                <Link href={`/pools/${index + 1}`}
                                    key={index}
                                    className='flex flex-col items-center justify-center gap-2 p-4 rounded-md bg-white shadow-md dark:bg-slate-800 dark:text-white transition-all cursor-pointer hover:shadow-xl hover:scale-105'
                                >
                                    <div
                                        className='w-full h-full rounded-full bg-gray-200'
                                    >
                                        <img src={Temp.src} alt="" />
                                    </div>
                                    <div
                                        className='flex items-center justify-between w-full mt-2'
                                    >
                                        <p className='font-regular text-lg leading-relaxed text-gray-800 dark:text-white'>
                                            Pool {index + 1}
                                        </p>
                                        <small className='text-gray-500'>
                                            230 images
                                        </small>
                                    </div>
                                </Link>
                            )
                        })
                    }
                </div>
            </div>
        </main >
    )
}

export default Pools;