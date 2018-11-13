import requests
import click
from random import randint
from download import download_image




def get_all_launches(spacex_api_url):
    response = requests.get(spacex_api_url)
    return response.json()


def find_all_complete_launches(launches):
    complete_launches = []
    for launch in launches:
        if launch.get('launch_success'):
            complete_launches.append(launch)
    return complete_launches


def find_last_launches(complete_launches, number):
    return complete_launches[-number::]


def get_launch_image_url(last_launches):
    all_images = []
    for launch in last_launches:
        links = launch.get('links')
        images = links.get('flickr_images')
        all_images.append(images)
    return all_images


def get_random_flickr_image(launches_images):
    random_images = []
    for launch_images in launches_images:
        random_number = randint(0, len(launch_images) -1)
        random_images.append(launch_images[random_number])
    return random_images


def spacex(number_of_launches):
    spacex_api_url = 'https://api.spacexdata.com/v3/launches'
    all_launches = get_all_launches(spacex_api_url)
    complete_launches = find_all_complete_launches(all_launches)
    last_complete_launches = find_last_launches(complete_launches, number_of_launches)
    launches_images = get_launch_image_url(last_complete_launches)
    random_images = get_random_flickr_image(launches_images)
    for url in random_images:
        download_image(url)


@click.command()
@click.option('--launches', default=5, help='Number of last spacex launches.')
def cli(launches):
    spacex(launches)


if __name__ == '__main__':
    cli()
