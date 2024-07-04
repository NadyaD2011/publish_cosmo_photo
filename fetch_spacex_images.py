from auxiliary_code import save_files, create_folder
import requests
import os
import argparse


def fetch_spacex_last_launch(folder_name, id, name_foto):
    image_link = f"https://api.spacexdata.com/v5/launches/{id}"
    response = requests.get(image_link)
    response.raise_for_status()
    photo_urls = response.json()['links']['flickr']['original']
    save_files(folder_name, photo_urls, name_foto)


def main():
    folder_name = 'images'
    name_foto = 'spacex'
    create_folder(folder_name)

    parser = argparse.ArgumentParser()
    parser.add_argument("--id", help="Ваш id", default='5eb87d47ffd86e000604b38a')
    args = parser.parse_args()
    id = args.id

    try:
        create_folder(folder_name)
        fetch_spacex_last_launch(folder_name, id, name_foto)
    except requests.exceptions.HTTPError as error:
        print("Can't get data from server:\n{0}".format(error))


if __name__ == '__main__':
    main()                  