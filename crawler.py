import re
import sys

__author__ = 'rbonick'

from bs4 import BeautifulSoup
import requests


class Crawler:
    def __init__(self):
        pass

    # noinspection PyMethodMayBeStatic
    def crawl(self, collection_url):
        # Get the website html and confirm it was successful
        response = requests.get(collection_url)
        response.raise_for_status()

        # Turn it into soup
        soup = BeautifulSoup(response.text)

        # Get the number of images
        num_images = int(soup.find(attrs={"data-reactid": re.compile(".2.2.1.1.1.1.4.1")}).string)

        # Iterate through the pages and grab the image urls
        img_urls = []
        for i in range(1, num_images + 1):
            print("On page {0} of {1}".format(i, num_images))
            outfit_url = collection_url + "/{0}".format(i)
            response = requests.get(outfit_url)
            soup = BeautifulSoup(response.text)

            # While this can find multiple html tags with .stretch-image,
            # the first is always the desired image tag
            img_tag = soup.select(".stretch-image")[0]
            img_urls.append(img_tag["src"])

        return img_urls


if __name__ == "__main__":
    crawler = Crawler()

    try:
        url = sys.argv[1]
    except IndexError:
        print("Please use this program in the format: "
              "'python crawler.py <collection slideshow url>'")
        url = None
    if url:
        results = crawler.crawl(url)
        for img_url in results:
            print(img_url)