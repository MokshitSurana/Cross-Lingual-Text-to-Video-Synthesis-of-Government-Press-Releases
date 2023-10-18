'use client'

/**These are necessary imports / components for the page */
import Text from "../components/Text/Text";
import FeaturedArticleSection from "../components/FeaturedArticleSection";
import LinkTo from "../components/LinkTo";
import { RxCross2 } from "react-icons/rx";
import { TextAlign } from "../shared/enums";
import { useState } from "react";
import { iArticle } from "../shared/interfaces";
import ArticleRead from "../components/ArticleRead";
import useMainContext from "../context/MainContext";
import Link from "next/link";

const Home = () => {

  const { selectedArtical } : any = useMainContext();
  return (
    <>
      <section className='w-full md:pt-[100px] md:pb-[70px] pt-[130px] pb-20 dark:bg-slate-800 bg-slate-200'>
        <div className="container text-center px-3">
          <Text title className='text-2xl md:text-4xl'>
            PressReleaseVid: Transforming Press Releases into Engaging Videos
          </Text>

          <Text p className="mt-3 text-base md:text-xl">
            Join us in revolutionizing information delivery through the fusion of technology and communication. Welcome to PressReleaseVid, where text meets the dynamic world of video!
          </Text>

          <div className='flex justify-center mt-5 flex-wrap '>
            <LinkTo href="#articles" className='flex items-center justify-center rounded-md bg-purple-500 px-4 pb-2 text-white hover:text-white shadow-lg hover:shadow-none transition-all mb-3 md:mx-5 mx-2'>
              <span className='text-base md:text-xl pt-2 block'>Get Started</span>
            </LinkTo>

            <Link href="/pools" className='flex items-center justify-center rounded-md bg-purple-500 px-4 pb-2 text-white hover:text-white shadow-lg hover:shadow-none transition-all mb-3 md:mx-5 mx-2'>
              <span className='text-base md:text-xl pt-2 block'>Pools</span>
            </Link>
          </div>
        </div>
      </section>
      <hr className="invisible mb-10" id="articles"/>
      <div className="container mx-auto lg:px-[15px] px-0 mt-16">
        <div className={'flex flex-wrap'}>
          <FeaturedArticleSection />
        </div>
      </div>

      {
        selectedArtical && (
          <ArticleRead />
        )
      }
    </>
  )
}

export default Home

