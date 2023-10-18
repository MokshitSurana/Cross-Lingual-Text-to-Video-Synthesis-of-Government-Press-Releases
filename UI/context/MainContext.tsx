'use client'

import { createContext, useContext, useState } from 'react'
import { iArticle } from '../shared/interfaces';

const MainContext = createContext({});

export function MainContextProvider({ children }: {
    children: React.ReactNode
}) {

    const [selectedArtical, setSelectedArtical] = useState<iArticle | null>(null)
    const [makeVideo, setMakeVideo] = useState<boolean>(false)

    const [script, setScript] = useState("");
    const [languages, setLanguages] = useState<string[]>([])

    return (
        <MainContext.Provider
            value={{
                selectedArtical, 
                setSelectedArtical,
                makeVideo,
                setMakeVideo,
                script,
                setScript,
                languages,
                setLanguages
            }}
        >
            {children}
        </MainContext.Provider>
    )
}


export default function useMainContext() {
    return useContext(MainContext);
}