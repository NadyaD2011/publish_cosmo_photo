from urllib.parse import urlparse, unquote, urlsplit
from datetime import datetime
import requests
import os

def create_folder(folder_name):
  if not os.path.exists(folder_name):
      os.makedirs(folder_name)


def fetch_spacex_last_launch(folder_name):
    launch_id = '5eb87d47ffd86e000604b38a'
    image_link = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = requests.get(image_link)
    response.raise_for_status()
    photo_urls = response.json()['links']['flickr']['original']
    for number_url, photo_url in enumerate(photo_urls):
        response = requests.get(photo_url)
        with open(f'{folder_name}/spacex{number_url}.jpg', 'wb') as file:
            file.write(response.content)


def create_image(folder_name):
    url = 'https://api.spacexdata.com/v5/launches/latest/'
    response = requests.get(url)
    response.raise_for_status()
    with open(f'{folder_name}/hubble.jpeg', 'wb') as file:
        file.write(response.content)

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
    for number_url, photo_url in enumerate(photo_urls):
        response = requests.get(photo_url)
        with open(f'{folder_name}/nasa_apod_{number_url}{get_extension(photo_url)}', 'wb') as file:
            file.write(response.content)

def save_epic_photo(folder_name, api_key):
    url = 'https://api.nasa.gov/EPIC/api/natural/image'
    params = {'api_key': api_key, 'count': 10}
    response = requests.get(url, params=params)
    response.raise_for_status()
    epic_images = response.json()
    photo_urls = []
    for epic_image in epic_images:
        file_name = epic_image["image"]
        epic_image_data = epic_image["date"]
        epic_image_data = datetime.datetime.fromisoformat(epic_image_data).strftime("%Y/%m/%d")
        link_path = f" https://api.nasa.gov/EPIC/archive/natural/ {epic_image_data}/png/{file_name}.png"
        photo_urls.append(link_path)

    del photo_urls[-13:-1]
    print(len(photo_urls))
    
    for number_url, photo_url in enumerate(photo_urls):
        response = requests.get(photo_url)
        with open(f'{folder_name}/nasa_epiс_{number_url}.png', 'wb') as file:
            file.write(response.content)
        
def main():
    api_key = os.environ['API_KEY']
    folder_name = 'images'
  
    create_folder(folder_name)
    create_image(folder_name)
    fetch_spacex_last_launch(folder_name)
    save_epic_photo(folder_name, api_key)
    save_photos_nasa(api_key, folder_name)


if __name__ == '__main__':
    main()