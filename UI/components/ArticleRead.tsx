import React from 'react'
import { useRouter } from 'next/navigation'
import Text from './Text/Text'
import { TextAlign } from '../shared/enums'
import { RxCross2 } from 'react-icons/rx'
import useMainContext from '../context/MainContext'

const ArticleRead = () => {

    const { setSelectedArtical , selectedArtical} : any = useMainContext();
    const router = useRouter();
    
    return (
        <div
            className="fixed z-20 top-0 bottom-0 left-0 right-0 bg-slate-800 bg-opacity-70 flex justify-center items-center"
        >
            <div className="absolute mx-auto top-8 bottom-8 w-[95%] md:w-[80%] bg-slate-100 dark:bg-slate-900 flex items-start px-3.5 md:px-12 pt-12 pb-28 justify-between h-[90lvh] rounded-2xl">
                <RxCross2
                    onClick={() => setSelectedArtical(null)}
                    className="text-slate-900 dark:text-white absolute top-2.5 right-2.5 text-3xl cursor-pointer"
                />
                <div
                    className="absolute bottom-7"
                >
                    <button
                        onClick={() => {
                            router.push('/script')
                        }}
                        className="relative px-5 py-2 font-medium text-white group">
                        <span className="absolute inset-0 w-full h-full transition-all duration-300 ease-out transform translate-x-0 -skew-x-12 bg-purple-500 group-hover:bg-purple-700 group-hover:skew-x-12"></span>
                        <span className="absolute inset-0 w-full h-full transition-all duration-300 ease-out transform skew-x-12 bg-purple-700 group-hover:bg-purple-500 group-hover:-skew-x-12"></span>
                        <span className="absolute bottom-0 left-0 hidden w-10 h-20 transition-all duration-100 ease-out transform -translate-x-8 translate-y-10 bg-purple-600 -rotate-12"></span>
                        <span className="absolute bottom-0 right-0 hidden w-10 h-20 transition-all duration-100 ease-out transform translate-x-10 translate-y-8 bg-purple-400 -rotate-12"></span>
                        <span className="relative text-white text-xl">Make Script</span>
                    </button>
                </div>
                <div className="overflow-y-auto h-full scrollbar-hide">
                    <Text title textAlign={TextAlign.CENTER} className="text-md md:text-3xl mt-0 w-full pb-12 sticky top-0 bg-slate-100 dark:bg-slate-900">
                        {
                            selectedArtical?.articleTitle
                        }
                    </Text>

                    <Text p className="text-sm md:text-xl whitespace-pre-wrap shadow-inset p-4 dark:bg-gray-800 w-full">
                        {
                            selectedArtical?.content
                        }
                    </Text>
                </div>
            </div>
        </div>
    )
}

export default ArticleRead