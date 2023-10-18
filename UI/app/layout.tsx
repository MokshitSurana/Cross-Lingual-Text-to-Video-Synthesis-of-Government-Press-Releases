'use client'
import './globals.scss'
import type { Metadata } from 'next'
import { ThemeProvider } from 'next-themes'
import { Component } from 'react'
import Footer from '../components/Footer'
import Navbar from '../components/Navbar'
import { MainContextProvider } from '../context/MainContext'
import { Toaster } from 'react-hot-toast'
import { motion, AnimatePresence } from 'framer-motion';
if (typeof window !== 'undefined') import('@dotlottie/player-component');

const metadata: Metadata = {
  title: 'SIH-1330',
  description: 'SIH-1330 | Team - 1330',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {

  return (
    <html lang="en"
      className=''
    >
      <head>
        <meta charSet="utf-8" />
        <meta name="description" content={metadata.description!} />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
        {/* <script type="text/javascript" id="MathJax-script" async
          src="https://cdn.jsdelivr.net/npm/mathjax@3.0.0/es5/tex-chtml.js">
        </script> */}
      </head>
      <body className={"bg-slate-100 dark:bg-slate-900 transition-all relative"}>
        <ThemeProvider enableSystem={true} attribute="class">
          <MainContextProvider>
            <AnimatePresence>
              <Navbar />
              <Toaster />
              {children}
              <Footer />
            </AnimatePresence>
          </MainContextProvider>
        </ThemeProvider>
      </body>
    </html>
  )
}
