import json
import requests
import re
import urllib.parse

import base64
from icrawler import ImageDownloader
from icrawler.builtin import GoogleImageCrawler
from six.moves.urllib.parse import urlparse

def _extractBingImages(html):
    pattern = r'mediaurl=(.*?)&amp;.*?expw=(\d+).*?exph=(\d+)'
    matches = re.findall(pattern, html)
    result = []

    for match in matches:
        url, width, height = match
        if url.endswith('.jpg') or url.endswith('.png') or url.endswith('.jpeg'):
            result.append({'url': urllib.parse.unquote(url), 'width': int(width), 'height': int(height)})

    return result


def getBingImages(query, retries=5, keywords='', filters=''):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
      'AppleWebKit/537.11 (KHTML, like Gecko) '
      'Chrome/23.0.1271.64 Safari/537.11',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
      'Accept-Encoding': 'none',
      'Accept-Language': 'en-US,en;q=0.8',
      'Connection': 'keep-alive'}
    query = query.replace(" ", "+")
    images = []
    tries = 0
    while(len(images) == 0 and tries < retries):
        response = requests.get(f"https://www.bing.com/images/search?q={query}+India+2023+{keywords}{filters}&first=1", headers=headers)
        if(response.status_code == 200):
            images = _extractBingImages(response.text)
        else:
            print("Error While making bing image searches", response.text)
            raise Exception("Error While making bing image searches")
    if(images):
        return images
    raise Exception("Error While making bing image searches")

def getGoogleImages(query, keywords):
    class getAttribution(ImageDownloader):
        def get_filename(self, task, default_ext):
            global word
            url = urlparse(task['file_url'])[0] + "://" +urlparse(task['file_url'])[1] + urlparse(task['file_url'])[2]
            filename = super(getAttribution, self).get_filename(
            task, default_ext)
            url_list.append(url)  # append url to the list
            return url

    google_crawler = GoogleImageCrawler(
    downloader_cls=getAttribution,
    downloader_threads=1,
    storage={'root_dir': 'test-delete'})

    search_query=query+' India 2023 Teachers day'
    url_list = []  # create an empty list to store urls

    google_crawler.crawl(search_query, max_num=5, filters = dict(
        type='photo'))
    return(url_list)
