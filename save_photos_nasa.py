from urllib.parse import urlparse, unquote, urlsplit
from dotenv import load_dotenv
import requests
import os

def create_folder(folder_name):
  if not os.path.exists(folder_name):
      os.makedirs(folder_name)

def get_extension(url):
    decoded_link = unquote(url)
    parsed_link = urlparse(decoded_link)
    path, fullname = os.path.split(parsed_link.path)
    file_extension_path = os.path.splitext(fullname)
    return file_extension_path[-1]

def save_photos_nasa(api_key, folder_name):
    photo_urls = []
    url = f'https://api.nasa.gov/planetary/apod'
    params = {'count': 30, "api_key": api_key}
    response = requests.get(url, params=params)
    response.raise_for_status()
    response = response.json()
    for photo_url in response:
        photo_urls.append(photo_url['url'])
    save_files(folder_name, photo_urls)    

def save_files(folder_name, photo_urls):
    for number_url, photo_url in enumerate(photo_urls):
        response = requests.get(photo_url)
        with open(f'{folder_name}/nasa_apod_{number_url}{get_extension(photo_url)}', 'wb') as file:
                file.write(response.content)

def main():
    load_dotenv()
    api_key = os.environ['API_KEY']
    folder_name = 'images'

    create_folder(folder_name)
    save_photos_nasa(api_key, folder_name)


if __name__ == '__main__':
    main()