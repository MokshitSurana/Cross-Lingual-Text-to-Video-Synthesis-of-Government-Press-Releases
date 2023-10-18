from shortGPT.api_utils.image_api import getBingImages, getGoogleImages
from tqdm import tqdm
import random
import math
import os
import requests
from imageio import imread
import shutil
from PIL import Image, ImageOps

def getImageUrlsTimed(imageTextPairs, keywords, listImageAssets=False):
    #print([(pair[0], searchImageUrlsFromQuery(pair[1])) for pair in tqdm(imageTextPairs, desc='Search engine queries for images...')])
    #return [(pair[0], searchImageUrlsFromQuery(pair[1], keywords=keywords, listImageAssets=listImageAssets)) for pair in tqdm(imageTextPairs, desc='Search engine queries for images...')]
    result = []
    urls = []
    for pair in tqdm(imageTextPairs, desc='Search engine queries for images...'):
        url = searchImageUrlsFromQuery(pair[1], keywords=keywords, listImageAssets=listImageAssets, urls=urls)
        urls.append(url)
        result.append((pair[0], url))
    shutil.rmtree('./test-delete')
    return result


from PIL import Image, ImageOps

def searchImageUrlsFromQuery(query, retries=5, keywords="", listImageAssets=False, urls=[]):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
      'AppleWebKit/537.11 (KHTML, like Gecko) '
      'Chrome/23.0.1271.64 Safari/537.11',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
      'Accept-Encoding': 'none',
      'Accept-Language': 'en-US,en;q=0.8',
      'Connection': 'keep-alive'}
    keywords = keywords
    if "president" in query:
        query+="+Droupadi+Murmu"
    images = getGoogleImages(query, keywords)
    filenames = []
    if(images):
        # best = images[0:3]
        # random.shuffle(best)
        # images = best + images[3:]
        for image in images:
            image_url = image
            print(image_url)
            try: 
                filename = os.getcwd()+"/resources/"+image_url.rsplit('/', 1)[-1]
                if filename in os.listdir(os.getcwd()+"/resources/"): 
                    return filename
                response = requests.get(image_url, headers=headers, timeout=5)
                with open(filename, "wb") as f:
                    f.write(response.content)
                try:
                    imread(filename)
                except:
                    os.remove(filename)
                    raise Exception("Image is not readable", image_url)
                if filename in urls: 
                    print("SKIPPED DUPLICATE")
                    continue
                # Open an image file
                img = Image.open(filename)
                # Add border
                border_color = (0, 0, 128)  # Navy blue in RGB
                border_width = 10  # Change this to the desired border width
                img_with_border = ImageOps.expand(img, border=border_width, fill=border_color)
                # Save the image file with a border
                img_with_border.save(filename)
                filenames.append(filename)
                if not listImageAssets or len(filenames) > 3:
                    break
            except Exception as e:
                print("Image DL Failed:", e, image_url)

        if listImageAssets:
            return filenames
        else:
            return filenames[0]
    raise Exception("Error While making bing image searches")
    return None
# def searchImageUrlsFromQuery(query, retries=5, keywords="", listImageAssets=False, urls=[]):
#     headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
#       'AppleWebKit/537.11 (KHTML, like Gecko) '
#       'Chrome/23.0.1271.64 Safari/537.11',
#       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
#       'Accept-Encoding': 'none',
#       'Accept-Language': 'en-US,en;q=0.8',
#       'Connection': 'keep-alive'}
#     keywords = keywords
#     #filters = '&qft=+filterui:photo-photo&adlt=on' #+filterui:age-lt525600
#     if "president" in query:
#         query+="+Droupadi+Murmu"
#     #images = getBingImages(query, retries=retries, keywords=keywords, filters=filters)
#     images = getGoogleImages(query, keywords)
#     filenames = []
#     if(images):
#         best = images[0:3]
#         random.shuffle(best)
#         images = best + images[3:]
#         for image in images:
#             image_url = image#['url']
#             print(image_url)
#             try: 
#                 filename = os.getcwd()+"/resources/"+image_url.rsplit('/', 1)[-1]
#                 if filename in os.listdir(os.getcwd()+"/resources/"): 
#                     return filename
#                 response = requests.get(image_url, headers=headers, timeout=5)
#                 with open(filename, "wb") as f:
#                     f.write(response.content)
#                 try:
#                     imread(filename)
#                 except:
#                     os.remove(filename)
#                     raise Exception("Image is not readable", image_url)
#                 if filename in urls: 
#                     print("SKIPPED DUPLICATE")
#                     continue
#                 filenames.append(filename)
#                 if not listImageAssets or len(filenames) > 3:
#                     break
#             except Exception as e:
#                 print("Image DL Failed:", e, image_url)

#         if listImageAssets:
#             return filenames
#         else:
#             return filenames[0]
#     raise Exception("Error While making bing image searches")
#     return None
#     # downloader.download(query=, limit=1, output_dir='missingImages', adult_filter_off=False, force_replace=False, timeout=60, verbose=False)