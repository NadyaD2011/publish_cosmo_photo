from auxiliary_code import save_files
import requests
import os
import argparse


def fetch_spacex_last_launch(fotos_arrived_id):
    foto_url = f"https://api.spacexdata.com/v5/launches/{fotos_arrived_id}"
    response = requests.get(foto_url)
    response.raise_for_status()
    photo_urls = response.json()['links']['flickr']['original']
    return photo_urls


def main():
    folder_name = 'images'
    name_foto_arrived = 'spacex'

    parser_id = argparse.ArgumentParser(description='Введите ваш id запуска')
    parser_id.add_argument("--id", help="Введите ваш id запуска", default='5eb87d47ffd86e000604b38a')
    args = parser_id.parse_args()
    fotos_arrived_id = args.id

    os.makedirs(folder_name, mode=0o777, exist_ok=True)
    photo_urls = fetch_spacex_last_launch(fotos_arrived_id)
    save_files(folder_name, photo_urls, name_foto_arrived)


if __name__ == '__main__':
    main()                  