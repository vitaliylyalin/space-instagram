import os
import time
import click
from instabot import Bot




def get_images_list(path='images'):
    return os.listdir(path)


def upload_photo(image, caption):
    bot.upload_photo(image, caption=caption)


def make_queue(path, images_list, timeout):
    for image in images_list:
        image = os.path.join(path, image)
        caption = 'random space image'
        upload_photo(image, caption)
        time.sleep(timeout)


@click.command()
@click.option('-t','--timeout', default=60, help='Interval in minutes between posts')
@click.option('-p','--path', default='images', help='Directory where images are stored')
def cli(timeout, path):
    images_list = get_images_list(path)
    timeout *= 60
    make_queue(path, images_list, timeout)


if __name__ == '__main__':
    bot = Bot()
    bot.login()
    cli()
