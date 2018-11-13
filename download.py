import os
import requests
from random import randint


def make_dir(name):
    if not os.path.exists(name):
        os.makedirs(name)


def download_image(url, path='images'):
    make_dir(name='images')
    img_data = requests.get(url).content
    image_extension = url.split('.')[-1]
    image_name = f'image{randint(1,9999)}.{image_extension}'
    with open(os.path.join(path, image_name), 'wb') as handler:
        handler.write(img_data)
