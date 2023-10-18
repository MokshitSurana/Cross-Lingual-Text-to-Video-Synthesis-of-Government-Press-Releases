'use client'

import React, { useEffect, useState } from 'react'
import { Socket, io } from 'socket.io-client'
import { iArticle } from '../shared/interfaces'
import Text from './Text/Text'
import { TextAlign } from '../shared/enums'
import { RxCross2 } from 'react-icons/rx'
import { useRouter } from 'next/navigation'
import useMainContext from '../context/MainContext'


type Props = {
    script: string,
    setModal: (arg: boolean) => void
}
const ViewScript = ({
    script,
    setModal
}: Props) => {

    return (
        <div
            className="fixed z-20 top-0 bottom-0 left-0 right-0 bg-slate-800 bg-opacity-70 flex justify-center items-center"
        >
            <div className="absolute mx-auto top-8 bottom-8 w-[95%] md:w-[80%] bg-slate-100 dark:bg-slate-900 flex items-start px-3.5 md:px-12 pt-10 pb-10 justify-between h-[90lvh] rounded-2xl">
                <RxCross2
                    onClick={() => {
                        setModal(false)
                    }}
                    className="text-slate-900 dark:text-white absolute top-2.5 right-2.5 text-3xl cursor-pointer"
                />
                <div className="overflow-y-auto h-full w-full scrollbar-hide">
                    <Text title textAlign={TextAlign.CENTER} className="text-md md:text-3xl mt-0 w-full pb-4 sticky -top-1 bg-slate-100 dark:bg-slate-900">
                        Generated Script
                    </Text>
                    <Text p className={`text-sm md:text-xl whitespace-pre-wrap shadow-inset p-4 dark:bg-gray-800`} >
                        {
                            script
                        }
                    </Text>
                </div>
            </div>
        </div>
    )
}

export default ViewScript