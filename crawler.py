import re
import sys
from urllib.parse import unquote
import json

__author__ = 'rbonick'

from bs4 import BeautifulSoup
import requests


class Crawler:
    def __init__(self):
        pass

    @staticmethod
    def crawl(collection_url):
        # Get the website html and confirm it was successful
        response = requests.get(collection_url)
        response.raise_for_status()

        # Turn it into soup
        soup = BeautifulSoup(response.text, "html.parser")

        # Grab the page's state json
        javascript = soup.find(id="initial-state")
        json_val = json.loads(unquote(javascript.string, 'utf-8'))

        # Retrieve all the slides
        slides = json_val['context']['dispatcher']['stores']['SlideshowStore']['data']['slides']

        # Iterate through the slides and grab the image urls
        img_urls = []
        for slide in slides:
            img_urls.append(slide['slidepath'])

        return img_urls


if __name__ == "__main__":
    try:
        url = sys.argv[1]
    except IndexError:
        print("Please use this program in the format: "
              "'python crawler.py <collection slideshow url>'")
        url = None
    if url:
        results = Crawler.crawl(url)
        for img_url in results:
            print(img_url)