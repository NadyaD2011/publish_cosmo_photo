from datetime import datetime
from dotenv import load_dotenv
from auxiliary_code import save_files
import requests
import os


def save_epic_photo(api_key):
    url = 'https://api.nasa.gov/EPIC/api/natural/image'
    foto_quantity = 10
    params = {'api_key': api_key, 'count': foto_quantity}
    response = requests.get(url, params=params)
    response.raise_for_status()
    epic_images = response.json()
    photo_urls = []
    for epic_image in epic_images:
        file_name = epic_image["image"]
        epic_image = epic_image["date"]
        epic_image = datetime.datetime.fromisoformat(epic_image).strftime("%Y/%m/%d")
        link_path = f"https://api.nasa.gov/EPIC/archive/natural/ {epic_image}/png/{file_name}.png"
        photo_urls.append(link_path)
    return photo_urls
        
def main():
    load_dotenv()
    api_key = os.environ['API_KEY_NASA']
    folder_name = 'images'
    names_foto = 'nasa_epiс_'
    
    os.makedirs(folder_name, mode=0o777, exist_ok=True)
    photo_urls = save_epic_photo(api_key)
    save_files(folder_name, photo_urls, names_foto)


if __name__ == '__main__':
    main()