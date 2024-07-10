from auxiliary_code import save_files, create_folder
import requests
import os
import argparse


def fetch_spacex_last_launch(folder_name, id, name_foto):
    foto_url = f"https://api.spacexdata.com/v5/launches/{id}"
    response = requests.get(foto_url)
    response.raise_for_status()
    photo_urls = response.json()['links']['flickr']['original']
    save_files(folder_name, photo_urls, name_foto)


def main():
    folder_name = 'images'
    name_foto = 'spacex'
    create_folder(folder_name)

    parser = argparse.ArgumentParser(description='Ваш id')
    parser.add_argument("--id", help="Ваш id", default='5eb87d47ffd86e000604b38a')
    args = parser.parse_args()
    id_arrived = args.id

    try:
        create_folder(folder_name)
        fetch_spacex_last_launch(folder_name, id_arrived , name_foto)
    except requests.HTTPError as error:
        print(f"Вы ввели неверный id, {error}")


if __name__ == '__main__':
    main()                  