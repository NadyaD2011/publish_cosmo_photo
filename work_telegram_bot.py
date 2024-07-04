from dotenv import load_dotenv
import telegram
import os
import argparse
import time
import requests
import random

def open_photos(frequency, bot, chat_id):
    while True:
        for root, dirs, files in os.walk("images"):  
            files = files

        random.shuffle(files)

        for filename in files:
            bot.send_document(chat_id=chat_id, document=open(f'images/{filename}', 'rb'))
            time.sleep(frequency*3600)

def main():
    parser = argparse.ArgumentParser(description='Частота отправки фото')
    parser.add_argument("--frequency", help="Частота отправки фото", default='4')
    args = parser.parse_args()
    frequency = args.frequency
    frequency = int(frequency)

    load_dotenv()
    chat_id = os.environ['CHAT_ID']
    bot = telegram.Bot(token=os.environ['TOKEN_BOT'])

    try:
        open_photos(frequency, bot, chat_id)
    except requests.exceptions.HTTPError as error:
        print("Can't get data from server:\n{0}".format(error))

if __name__ == "__main__":
    main()