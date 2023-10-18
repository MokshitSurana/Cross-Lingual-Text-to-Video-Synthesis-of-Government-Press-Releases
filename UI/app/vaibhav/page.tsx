"use client";
import React, { useState, useEffect } from "react";
import useMainContext from "../../context/MainContext";
import MakeVideo from "../../components/MakeVideo";
import ViewScript from "../../components/ViewScript";
import data from "../vaibhav/data.json";
import ModalImage from "../../components/ModalImage";
type Props = {};

const VideoMaker = (props: Props) => {
  const { script }: any = useMainContext();

  const [modal, setModal] = useState(false);

  return (
    <main className="container py-20 md:py-6">
      <h1 className="text-3xl md:text-5xl font-bold text-center mb-10 md:mb-20 ">
        Script Image Picker for Video Maker
      </h1>
      <div className="flex flex-col">
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
        <button
          onClick={() => setModal(true)}
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold m-10 px-2 px-4 rounded"
        >
          Generate Video
        </button>
        {modal && <ViewScript setModal={setModal} script={script} />}
      </div>
    </main>
  );
};

export default VideoMaker;
