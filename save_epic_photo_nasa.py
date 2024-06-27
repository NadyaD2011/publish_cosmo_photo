from datetime import datetime
from dotenv import load_dotenv
import requests
import os

def create_folder(folder_name):
  if not os.path.exists(folder_name):
      os.makedirs(folder_name)

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
    save_photo(photo_urls, folder_name)
    
def save_photo(photo_urls, folder_name):
    for number_url, photo_url in enumerate(photo_urls):
        response = requests.get(photo_url)
        with open(f'{folder_name}/nasa_epiс_{number_url}.png', 'wb') as file:
            file.write(response.content)
        
def main():
    load_dotenv()
    api_key = os.environ['API_KEY']
    folder_name = 'images'
  
    create_folder(folder_name)
    save_epic_photo(folder_name, api_key)


if __name__ == '__main__':
    main()