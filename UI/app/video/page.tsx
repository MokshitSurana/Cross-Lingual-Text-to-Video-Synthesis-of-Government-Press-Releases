'use client'
import React, { useState, useEffect } from 'react'
import useMainContext from '../../context/MainContext'
import MakeVideo from '../../components/MakeVideo'
import ViewScript from '../../components/ViewScript'
type Props = {}

const VideoMaker = (props: Props) => {
    const { script }: any = useMainContext();

    const [modal, setModal] = useState(false);

    useEffect(() => {
        // if (!script) {
        //     alert("No script Found!")
        //     router.push("/")
        // }
    }, [])

    return (
        <main className='container py-20 md:py-6'>
            <div className='flex flex-col'>
                <button className={`self-start flex items-center justify-center rounded-md bg-purple-500 text-white hover px-4 pb-2 shadow-lg hover:shadow-none transition-all mb-3`}
                    onClick={() => {
                        setModal(true)
                    }}
                >
                    <span className='text-base md:text-xl pt-2 block'>View Script</span>
                </button>
                {
                    modal && <ViewScript script={script} setModal={setModal} />
                }
                <MakeVideo />
            </div>
        </main >
    )
}

export default VideoMaker;