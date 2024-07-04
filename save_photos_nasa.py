from dotenv import load_dotenv
from auxiliary_code import save_files, create_folder
import requests
import os


def save_photos_nasa(api_key, folder_name, name_foto):
    photo_urls = []
    url = f'https://api.nasa.gov/planetary/apod'
    params = {'count': 30, "api_key": api_key}
    response = requests.get(url, params=params)
    response.raise_for_status()
    response = response.json()
    for photo_url in response:
        photo_urls.append(photo_url['url'])
    save_files(folder_name, photo_urls, name_foto)    


def main():
    load_dotenv()
    api_key = os.environ['API_KEY_NASA']
    folder_name = 'images'
    name_foto = 'nasa_apod_'

    create_folder(folder_name)
    save_photos_nasa(api_key, folder_name, name_foto)


if __name__ == '__main__':
    main()