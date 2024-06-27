import requests
import os

def create_folder(folder_name):
  if not os.path.exists(folder_name):
      os.makedirs(folder_name)

def fetch_spacex_last_launch(folder_name, id):
    image_link = f"https://api.spacexdata.com/v5/launches/{id}"
    response = requests.get(image_link)
    response.raise_for_status()
    photo_urls = response.json()['links']['flickr']['original']
    save_files(folder_name, photo_urls)

def save_files(folder_name, photo_urls):
    for number_url, photo_url in enumerate(photo_urls):
        response = requests.get(photo_url)
        with open(f'{folder_name}/spacex{number_url}.jpg', 'wb') as file:
            file.write(response.content)

def main():
    folder_name = 'images'
    id = argparse.ArgumentParser()
    id.add_argument("id", help="Ваш id")
    id = parser.parse_args()
    id = id.id

    create_folder(folder_name)

    try:
        if id != '':
            fetch_spacex_last_launch(folder_name, id)
        else:
            fetch_spacex_last_launch(folder_name, id='latest')
    except requests.exceptions.HTTPError as error:
        print("Can't get data from server:\n{0}".format(error))


if __name__ == '__main__':
    main()                  