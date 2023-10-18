
import React from 'react'

type Props = {}

const AddImageModal = (props: Props) => {
  return (
    <div>AddImageModal</div>
  )
}

export default AddImageModal


// import React, { useState } from 'react'
// import { RxCross2 } from 'react-icons/rx';


// const AddImageModal = () => {

//     const [image, setImage] = useState<File | null>(null);

//     const submitHandler = () => {
//         // if (image) {
//         // const reader = new FileReader();
//         // reader.readAsDataURL(image);
//         // reader.onloadend = () => {
//         //     setModelUri(reader.result);
//         //     setModelThumbnail("");
//         //     setUploadModal(false);
//         //     setTitle(
//         //         image.name.
//         //             replace(".glb", "").
//         //             replace(".gltf", "")
//         //     );
//         // };
//         // }
//     }

//     return (
//         <div
//             className="absolute top-0 left-0 right-0 bottom-0 z-[200] w-full"
//             aria-labelledby="modal-title"
//             role="dialog"
//             aria-modal="true"
//         >
//             <div className="absolute top-0 left-0 right-0 bottom-0 bg-gray-800 bg-opacity-40 transition-opacity" />
//             <div className="absolute top-0 left-0 right-0 bottom-0 z-10 overflow-y-auto flex flex-col gap-4 items-center justify-center">

//                 <div className="flex items-center justify-center w-[80%]">
//                     <label
//                         htmlFor="dropzone-file"
//                         className="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50"
//                     >
//                         <div className="flex flex-col items-center justify-center pt-5 pb-6">
//                             <svg
//                                 className="w-8 h-8 mb-4 text-gray-500"
//                                 aria-hidden="true"
//                                 xmlns="http://www.w3.org/2000/svg"
//                                 fill="none"
//                                 viewBox="0 0 20 16"
//                             >
//                                 <path
//                                     stroke="currentColor"
//                                     strokeLinecap="round"
//                                     strokeLinejoin="round"
//                                     strokeWidth={2}
//                                     d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"
//                                 />
//                             </svg>
//                             {
//                                 image ? (
//                                     <div className="relative w-32 h-32 p-2 border-2 border-gray-300 rounded-xl">
//                                         <img
//                                             className="w-full h-full object-cover rounded-xl"
//                                             src={URL.createObjectURL(image)}
//                                             alt="Image"
//                                         />
//                                         <button
//                                             className="absolute -top-4 -right-4 w-8 h-8 bg-red-500 rounded-full flex items-center justify-center"
//                                             onClick={(e) => {
//                                                 e.preventDefault();
//                                                 setImage(null)
//                                             }}
//                                         >
//                                             <RxCross2 className="w-4 h-4 text-white" />
//                                         </button>
//                                     </div>
//                                 ) : (
//                                     <>
//                                         <p className="mb-2 text-sm text-gray-500">
//                                             <span className="font-semibold">Click to upload</span> or drag and drop
//                                         </p>
//                                         <p className="text-xs text-gray-500">
//                                             GLB or GLTF files up to 100mb
//                                         </p>
//                                     </>
//                                 )
//                             }
//                         </div>
//                         <input
//                             id="dropzone-file"
//                             type="file"
//                             accept=".png,.jpg,.jpeg,.webp"
//                             onChange={(e) => {
//                                 // console.log(e.target.files[0]);
//                                 if (e.target.files) setImage(e.target.files[0]);
//                             }}
//                             className="hidden"
//                         />
//                     </label>
//                 </div>
//             </div>
//         </div>

//     )
// }

// export default AddImageModal;