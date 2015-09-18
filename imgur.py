from imgurpython.helpers.error import ImgurClientError, ImgurClientRateLimitError
import time

__author__ = 'rbonick'

from imgurpython import ImgurClient

import secrets


def authenticate():
    try:
        client = ImgurClient(secrets.client_id, secrets.client_secret)
        return client
    except ImgurClientError as e:
        print(e.error_message)
        print(e.status_code)
        return None


def create_album(client, album_name, image_urls):
    try:
        album_config = {}
        if album_name:
            album_config['title'] = album_name
        album = client.create_album(album_config)
        album_hash = album['deletehash']
        for i, url in enumerate(image_urls):
            print("Uploading image {} of {}".format(i + 1, len(image_urls)))
            upload_image(client, url, album_hash)
        return create_link_from_id(album['id'])
    except ImgurClientError as e:
        print(e.error_message)
        print(e.status_code)
        return "An error occurred."
    except ImgurClientRateLimitError:
        client.get_credits()
        print("Rate limit hit. User uploads remaining: {}. Client uploads remaining: {}".format(
            client.credits['UserRemaining'], client.credits['ClientRemaining']))
        return "An error occurred."


def upload_image(client, image_url, album):
    if int(client.credits['UserRemaining']) < 10:
        print("Upload limit reached. Sleeping for an hour.")
        time.sleep(3600)
    image_config = {"album": album}
    image = client.upload_from_url(image_url, image_config)
    print("Uploads remaining before timeout {}".format(client.credits['UserRemaining']))
    return image['id']


def create_link_from_id(id):
    return "http://imgur.com/a/{}".format(id)


def check_rate_limit(client):
    print("User uploads remaining: {}. Client uploads remaining: {}".format(client.credits['UserRemaining'],
                                                                            client.credits['ClientRemaining']))


if __name__ == "__main__":
    check_rate_limit(authenticate())