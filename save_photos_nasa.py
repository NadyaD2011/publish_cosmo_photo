from dotenv import load_dotenv
from auxiliary_code import save_files
import requests
import os


def save_photos_nasa(api_key):
    photo_urls = []
    url = f'https://api.nasa.gov/planetary/apod'
    foto_quantity = 30
    params = {'count': foto_quantity, "api_key": api_key}
    response = requests.get(url, params=params)
    response.raise_for_status()
    response = response.json()
    for photo_url in response:
        photo_urls.append(photo_url['url'])   
    return photo_url    


def main():
    load_dotenv()
    api_key = os.environ['API_KEY_NASA']
    folder_name = 'images'
    name_foto = 'nasa_apod_'

    os.makedirs(folder_name, mode=0o777, exist_ok=True)
    photo_urls = save_photos_nasa(api_key)
    save_files(folder_name, photo_urls, name_foto) 


if __name__ == '__main__':
    main()