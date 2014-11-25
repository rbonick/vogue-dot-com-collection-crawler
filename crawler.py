import re

__author__ = 'rbonick'

from bs4 import BeautifulSoup
import requests


class Crawler:
    def __init__(self):
        pass

    def crawl(self, url):
        # Get the website html and confirm it was successful
        response = requests.get(url)
        response.raise_for_status()

        # Turn it into soup
        soup = BeautifulSoup(response.text)

        # print(soup.prettify())

        # Get the number of images
        num_images = int(soup.find(attrs={"data-reactid": re.compile(".2.2.1.1.1.1.4.1")}).string)

        # Iterate through the pages and grab the image urls
        img_urls = []
        for i in range(1, num_images + 1):
            print("On page {0} of {1}".format(i, num_images))
            outfit_url = url + "/{0}".format(i)
            response = requests.get(outfit_url)
            soup = BeautifulSoup(response.text)

            # While this can find multiple html tags with .stretch-image, the first is always the desired image tag
            img_tag = soup.select(".stretch-image")[0]
            img_urls.append(img_tag["src"])

        return img_urls


if __name__ == "__main__":
    crawler = Crawler()
    # results = crawler.crawl("http://www.style.com/slideshows/fashion-shows/spring-2015-ready-to-wear/chanel/collection")
    results = crawler.crawl("http://www.style.com/slideshows/fashion-shows/fall-2014-couture/maison-martin-margiela/collection")
    for url in results:
        print(url)