
# 🚀🎬 PIB GenMotion AI
![Logo](https://res.cloudinary.com/dgccztjql/image/upload/v1695878803/sih/logo_2_ae2wwn.png)

## 🎥 Showcase ([Full video on YouTube](https://youtu.be/F-C8H0U3_QQ?feature=shared)) ([English Demo on Youtube](https://youtube.com/shorts/u4i3fN9t9cE?si=m5XGg4BN6sr-a7rG))

## 🌟 Abstract
The solution provides a `robust` and `efficient` approach for the conversion of PIB press releases to engaging videos with the use of `Artificial Intelligence` and Generative Adversarial Networks. It provides a `streamlined dissemination` of press articles through multimedia platforms. The entire process begins with the `selection of an article`, made by the PIB Officer. The article is then `summarized` with the help of a natural language summarization algorithm to condense the article for relevant points. The `Large Language Model` morphs the summarized article into an engaging `video script`, which can be reviewed and edited by the PIB Officer, before being sent to the backend for the video generation process. Parallel processes occur simultaneously in the backend, whereby the LLaMA model browses for high-quality, relevant and `copyright-free images` from the `image pool` stored in the database, as well as over the internet, along with the script translated in `13 regional languages` using Google Translate. Furthermore, voice `narration` and segmented `timed captions` are generated using Microsoft Text to Speech (TTS). These visual and audio assets are then passed through MoviePy, to be utilized by FFmpeg and ImageMagick for adding `transitions` and `animations` to the generated video. These processes lead to the rendering of the final videos in all languages, upon which a `notification` is sent to the concerned PIB Officer for the final evaluation. Once the generated videos are approved, the videos are then uploaded to the respective `PIB social media accounts`, automatically without the intervention of the PIB Officer. These videos are `analyzed` for statistical data, which can be used by the PIB Officer to gain `additional insights` about the outreach of the article on all social media platforms. The solution also allows the PIB Officer to create `daily summary videos`, adding highlighted videos for a particular day in a single video. The `image pool` used in the video generation process can be created and modified by the PIB Officer, where the images uploaded have automated captions generated with the help of Git Coco. Overall, the solution `automates` all necessary processes for generation of a video, eliminating manual work overload, and enables the content to reach a `larger audience`.

## 🛠️ How it works
![alt text](https://res.cloudinary.com/dgccztjql/image/upload/v1695877534/sih/Flowchart_25_hmaezg.png)
## 📝 Introduction to GenMotion AI 
GenMotion AI is a powerful framework for automating content creation. It simplifies video creation, voiceover synthesis, animated layouts, and editing tasks.

- 🎞️ **Automated editing framework**: Streamlines the video creation process with an LLM oriented video editing language.

- 📃 **Scripts and Prompts**: Provides ready-to-use scripts and prompts for various LLM automated editing processes.

- 🗣️ **Voiceover / Content Creation**: Supports multiple languages including English 🇮🇳, Hindi 🇮🇳, Urdu 🇵🇰, Punjabi 🇮🇳, Gujarati 🇮🇳, Marathi 🇮🇳, Telugu 🇮🇳, Kannada 🇮🇳, Malayalam 🇮🇳, Tamil 🇮🇳, Odia 🇮🇳, Bengali 🇮🇳, Assamese 🇮🇳, and Manipuri 🇮🇳. (with Microsoft TTS)

- 🔗 **Caption Generation**: Automates the generation of video captions.

- 🌐🎥 **Asset Sourcing**: Sources images from the internet, connecting with the web and the image pool from the database as necessary.

## 📄 Description
### 📇 Dashboard Selection
Upon signing in, the officer encounters a dashboard displaying four options, each offering unique functionalities to streamline the dissemination of vital information through engaging multimedia formats. This intuitive dashboard serves as the gateway to harnessing cutting-edge technology for effective communication and outreach. Let's dive into each of these options:

### 🎥 Create a Video from a Press Release
- **Choosing a Press Release:** Within the "Create Video" option, the officer is presented with a library of press releases available on the site. They carefully browse through this repository and choose a specific press release that they wish to summarize.

- **Text Summarization:** The full text of the selected press release undergoes a sophisticated natural language summarization algorithm known as "pegasus-cnn_dailymail." This cutting-edge technology extracts the most vital and relevant points from the press release and distills them into a concise summary that captures the essence of the content in just a few sentences.

- **Script Generation:** The summary, generated in the previous step, serves as input for the LLaMa natural language generation model. LLaMa then analyzes the content and automatically generates a script for the video. This script includes structuring the key messages in a logical sequence, crafting concise voiceover narration, and scheduling when each point should be narrated.

- **Draft Script Review:** The draft script is presented to the officer for meticulous review and editing. This crucial step allows the officer to refine and polish the script, ensuring its perfection and alignment with the intended message.

- **Multilingual Translation:** Once the script is finalized, it triggers two parallel processes. Google Translate swiftly converts the script into 13 official regional languages, ensuring broader accessibility.

- **Image Selection:** Simultaneously, the LLaMa model searches the web for copyright-free images and accesses an internal database containing a pool of relevant visuals that correspond to the script. It compiles a selection of images with suitable captions for the officer to choose from.

- **Officer's Image Curation:** The officer curates the images, selecting the most appropriate ones to visually complement the narration. This step involves a careful choice to enhance the overall impact of the video.

- **Voiceover Synthesis:** Microsoft's advanced neural text-to-speech engine is employed to synthesize professional voiceovers from the finalized script in all 13 languages, ensuring consistent and high-quality narration.

- **Video Rendering:** The approved images are combined with the audio, and using moviepy library in Python the video is created. This process includes adding polished transitions like fade-outs and flips to create an engaging and seamless video sequence.

- **Multilingual Video Rendering:** The completed videos are rendered in each of the 13 regional languages, expanding the video's reach and accessibility.

- **Notification and Publishing:** Once the rendering is complete, the officer receives a notification informing them that the summarized press release videos are ready for publishing. These videos can be shared across various social media platforms such as YouTube, Instagram, X, and Facebook to reach the intended audience.

### 🎞️ Create a Daily Summary Video
- **Selection:** In this option, the PIB Officer has the capability to create a summary video encompassing all the press releases posted on a particular day. This allows viewers to gain a comprehensive understanding of the day's events.

- **Process Similarity:** The process for creating this daily summary video is akin to the first option, involving text summarization, script generation, multilingual translation, image selection, voiceover synthesis, and video rendering. However, it is important to note that the rendering time is extended due to the inclusion of multiple press releases, estimated at approximately 30 to 40 minutes.

### 🗂️ Create a New Image Album
- **Album Creation:** In the third option, the PIB Officer can initiate the creation of a new image album.

- **Captioning by Git Coco:** The images within this album are captioned using the Git Coco model. This involves automatically generating descriptive captions for each image. For example, if a photo features President Draupadi Murmu, the caption would include their name.

- **Database Addition:** The album of captioned images is then added to the PIB's image database, enriching its content and making it more informative.

### 📸 Add Images to an Existing Album
- **Image Addition:** In this option, the PIB Officer has the ability to augment an existing image album by adding new images.

- **Processing Parallels:** The new images undergo the same steps as in the third option, including captioning by the Git Coco model, before being incorporated into the existing album.

### 📊 View Video Analytics and Feedback
- **Analytics Access:** This option allows the PIB Officer to access video analytics, providing valuable insights into how viewers interact with the videos. The officer can examine specific details such as the times at which people watch the videos, their geographic locations, and more.
- **Utilization for Scheduling:** These analytics can be instrumental in optimizing video scheduling to maximize reach and engagement among the audience.


<!-- ## ⚙️ Tech Stack

| Name                       | Description |
| -------------------------- | ------------------------------------------------------------ |
| ![alt](https://res.cloudinary.com/dgccztjql/image/upload/v1695885054/sih/next_mr8rav.png) | Next.js is a React framework used for building server-rendered web applications. It provides us with features like server-side rendering, routing, and static site generation. |
| ![alt](https://res.cloudinary.com/dgccztjql/image/upload/v1695886924/sih/tailwind_qnf2ru.png) | Tailwind CSS is a utility-first CSS framework that makes it easy to style web applications by applying predefined classes to HTML elements.It is used for styling our PIB portal. |
| ![alt](https://res.cloudinary.com/dgccztjql/image/upload/v1695886923/sih/Llama_qj9g44.png) | Your GitHub username |
| ![alt](https://res.cloudinary.com/dgccztjql/image/upload/v1695886925/sih/socket_ytu7lc.png) | Your full name |
| ![alt](https://res.cloudinary.com/dgccztjql/image/upload/v1695886924/sih/python_nua2jh.png) | Your full name |
| ![alt](https://res.cloudinary.com/dgccztjql/image/upload/v1695886923/sih/flask_rijl3d.png) | Full OSS license name |
| ![alt](https://res.cloudinary.com/dgccztjql/image/upload/v1695886924/sih/pytorch_nnpjph.png) | Use HTML to prettify your header |
| ![alt](https://res.cloudinary.com/dgccztjql/image/upload/v1695887707/sih/moviepy_rgdyvu.png) | Use table to wrap around About section |
| ![alt](https://res.cloudinary.com/dgccztjql/image/upload/v1695886924/sih/imagemagick_mmhymt.png) | Include Logo section. Only valid when `modern_header == y` |
| ![alt](https://res.cloudinary.com/dgccztjql/image/upload/v1695886923/sih/ffmpeg_cz9yvz.png) | Include section for badges |
| ![alt](https://res.cloudinary.com/dgccztjql/image/upload/v1695886925/sih/vtt_guwkhu.png) | Include Table of Contents |
| ![alt](https://res.cloudinary.com/dgccztjql/image/upload/v1695886923/sih/langchain_jfp0dg.png) | Include Screenshots section |
| ![alt](https://res.cloudinary.com/dgccztjql/image/upload/v1695886924/sih/node_zw9mby.png) | Include Project assistance section |
| ![alt](https://res.cloudinary.com/dgccztjql/image/upload/v1695886924/sih/mongodb_hjupcl.png) | Include Authors & contributors section | -->

## 🎞️ Demo Videos for Regional Languages

| Hindi                      | Marathi                    | Gujarati                   |                  
| :------------------------: | :------------------------: | :------------------------: |
| [![alt](https://res.cloudinary.com/dgccztjql/image/upload/v1696094794/sih/Hindi_qd2awi.png)](https://youtube.com/shorts/BVI6r8SXsTA?si=pdhGJoDfjgu4ufsp) | [![alt](https://res.cloudinary.com/dgccztjql/image/upload/v1696094795/sih/Marathi_xd4uwv.png)](https://youtube.com/shorts/wd-bRVdoGSs?si=IfaSJtMRsp7Lc_-u) | [![alt](https://res.cloudinary.com/dgccztjql/image/upload/v1696094794/sih/Gujarati_dbuvnt.png)](https://youtube.com/shorts/SnwbZYEC51w?si=ZHQvKLEUgNgpnQl0) | 

| Tamil                   | Telugu                      | Kannada                    |
| :------------------------: | :------------------------: | :------------------------: |
| [![alt](https://res.cloudinary.com/dgccztjql/image/upload/v1696094797/sih/Tamil_floxvg.png)](https://youtube.com/shorts/3Uw1WAbb2Xw?si=2cNjZgqK7HgiwuLL) | [![alt](https://res.cloudinary.com/dgccztjql/image/upload/v1696094798/sih/Telugu_wcg1bv.png)](https://youtube.com/shorts/w9euDVBHXf0?si=7Uhy8sibVPEMixqE) | [![alt](https://res.cloudinary.com/dgccztjql/image/upload/v1696094795/sih/Kannada_cjclqa.png)](https://youtube.com/shorts/h9Xj6zR0Oac?si=c9eBa-Cy-PZ7VPLn) |

| Urdu                      | Malayalam                    | Bengali |
| :------------------------: | :------------------------: | :------------------------: | 
|  [![alt](https://res.cloudinary.com/dgccztjql/image/upload/v1696094798/sih/Urdu_uqqmue.png)](https://youtube.com/shorts/85QAwzTmdxI?si=cRu2z3_s_6la9y8k) | [![alt](https://res.cloudinary.com/dgccztjql/image/upload/v1696094794/sih/Malayalam_p81bvt.png)](https://youtube.com/shorts/c-Eh9uFyAAA?si=YJPYi0HHr4eDUq83) | [![alt](https://res.cloudinary.com/dgccztjql/image/upload/v1696094794/sih/Bengali_p3zxeh.png)](https://youtube.com/shorts/oIGt0tsD2vY?si=XVeCsSZ543LRFSSr) |
