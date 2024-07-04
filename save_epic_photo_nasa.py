from datetime import datetime
from dotenv import load_dotenv
from auxiliary_code import save_photo, create_folder
import requests
import os


def save_epic_photo(folder_name, api_key, names_foto):
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
        
    save_photo(photo_urls, folder_name, names_foto)
        
def main():
    load_dotenv()
    api_key = os.environ['API_KEY_NASA']
    folder_name = 'images'
    names_foto = 'nasa_epiс_'
  
    create_folder(folder_name)
    save_epic_photo(folder_name, api_key, names_foto)


if __name__ == '__main__':
    main()