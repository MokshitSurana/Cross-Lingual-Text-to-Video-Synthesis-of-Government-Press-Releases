
import os, random, shutil
from PIL import Image
import numpy as np
from icrawler.builtin import GoogleImageCrawler
import difPy
def isDuplicate():
    # encodings = phasher.encode_images(image_dir='./tmp_images/AAselected')
    # duplicates = phasher.find_duplicates(encoding_map=encodings)
    # print(duplicates.keys())
    # return False#img in duplicates.keys()
    dif = difPy.build('./tmp_images/AAselected/')
    search = difPy.search(dif)
    print(search.result)
    return len(search.result.keys())

def getImagesfromQueries(queries, keywords=''):
    if not os.path.exists('./tmp_images/AAselected'):
        os.mkdir('./tmp_images/AAselected')
    for files in os.listdir('./tmp_images/AAselected'):
        os.remove('./tmp_images/AAselected/'+files)
    filters = {
        'type':'photo',
        #'license':'commercial',
        'date':((2022, 1, 1), None)
        }
    output = []
    for query in queries:
        path = './tmp_images/'+query
        if True:#not os.path.exists(path):
            google_crawler = GoogleImageCrawler(storage={'root_dir': path}, parser_threads=5, downloader_threads=5)
            google_crawler.crawl(keyword=f'{query} ({keywords})', max_num=5, filters=filters, overwrite=False, min_size=(400,400), language='in')
        images = sorted(os.listdir(path))
        i=0
        if len(output)>0:
            for image in images:
                    shutil.copyfile(path+'/'+image, f'./tmp_images/AAselected/0.jpg')
                    if isDuplicate():
                        i+=1
                    else:
                        break

                    if image==images[-1]:
                        i=0
                        break
        shutil.copyfile(path+'/'+images[i], f'./tmp_images/AAselected/{len(output)+1}.jpg')
        output.append(path+'/'+images[i])
    return output