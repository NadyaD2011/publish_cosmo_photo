from dotenv import load_dotenv
from save_foto import save_files
import requests
import os

def create_folder(folder_name):
  if not os.path.exists(folder_name):
      os.makedirs(folder_name)

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
    api_key = os.environ['API_KEY']
    folder_name = 'images'
    name_foto = 'nasa_apod_'

    create_folder(folder_name)
    save_photos_nasa(api_key, folder_name, name_foto)


if __name__ == '__main__':
    main()