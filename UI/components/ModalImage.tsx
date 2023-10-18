"use client";
import React, { useEffect, useState } from "react";
import { ImCancelCircle } from "react-icons/im";
import { motion } from "framer-motion";
type Props = {
  script: string;
  setModal?: (arg: boolean) => void;
  imageList: string[];
  timeStamp: string[];
};

const ViewScript = ({ script, setModal, imageList, timeStamp }: Props) => {
  const [imageShow, setImageShow] = useState(false);
  const [selectedImage, setSelectedImage] = useState(0);
  return (
    <div>
      <a
        className={`cursor-pointer  ${imageShow ? "font-bold" : ""}`}
        onClick={() => setImageShow(!imageShow)}
      >
       <span className="font-semibold">{timeStamp[0] + " - " + timeStamp[1] + " : "}</span>
        {script}
      </a>
      {imageShow && (
        <div className="p-2 shadow-lg rounded-md bg-purple-200 bg-opacity-70 ">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-x-36 ">
            <div className="grid grid-flow-row">
              <h1 className="font-semibold text-black">Pick Images:</h1>
              <div className="grid grid-cols-3 gap-3">
                {imageList.map((image, i) => {
                  return (
                    <motion.img
                      initial={{ scale: 0 }}
                      animate={{ rotate: 0, scale: 1 }}
                      transition={{
                        type: "spring",
                        stiffness: 260,
                        damping: 50,
                      }}
                      alt=""
                      className={`cursor-pointer  ${
                        selectedImage === i
                          ? "border-4 rounded-md border-blue-500"
                          : "border rounded-md border-gray-200"
                      }`}
                      key={i}
                      src={image}
                      onClick={() => {
                        setSelectedImage(i);
                      }}
                    />
                  );
                })}
              </div>
            </div>
            
            <div className="grid ">
            <h1 className="font-semibold text-black">Selected Images: </h1>
              <div className="grid grid-cols-1 justify-center  w-1/2">
                <motion.img
                  initial={{ scale: 0  }}
                  animate={{ rotate: 0, scale: 1 }}
                  transition={{
                    type: "spring",
                    stiffness: 260,
                    damping: 50,
                  }}
                  alt=""
                  className="border-4 rounded-md border-blue-500"
                  src={imageList[selectedImage]}
                />
              </div>
            </div>
            <ImCancelCircle
            onClick={() => setImageShow(false)}
            className="text-slate-900 dark:text-white right-2  absolute cursor-pointer"
          />
          </div>
        </div>
      )}
    </div>
  );
};

export default ViewScript;
