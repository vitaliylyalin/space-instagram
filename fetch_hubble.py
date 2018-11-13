import requests
import click
from download import download_image




def get_images_id_from_collection(collection):
    url = f'http://hubblesite.org/api/v3/images/{collection}?page=all'
    images_id = []
    response = requests.get(url)
    for image in response.json():
        images_id.append(image.get('id'))
    return images_id


def get_files_from_images_id(images_id):
    images_files = []
    for id in images_id:
        url = f'http://hubblesite.org/api/v3/image/{id}'
        response = requests.get(url)
        response_json = response.json()
        images_files.append(response_json.get('image_files'))
    return images_files


def get_images_urls(images_files, number_of_urls):
    images_urls = []
    for image in images_files:
        images_urls.append(image[0].get('file_url'))
    return images_urls[:number_of_urls]


def hubble(collection, number_of_images, path):
    images_id = get_images_id_from_collection(collection)
    images_files = get_files_from_images_id(images_id)
    images_urls = get_images_urls(images_files, number_of_images)
    for url in images_urls:
        download_image(url, path)


@click.command()
@click.option('-c','--collection', default='wallpaper', help='Collection of images on the Hubblesite')
@click.option('-i','--images', default=10, help='Maximum number of images')
@click.option('-p','--path', default='images', help='Directory where images will store')
def cli(collection, images, path):
    hubble(collection, images, path)


if __name__ == '__main__':
    cli()
