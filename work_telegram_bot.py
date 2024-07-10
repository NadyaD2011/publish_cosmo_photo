from dotenv import load_dotenv
import telegram
import os
import argparse
import time
import requests
import random

def publish_photos(frequency, bot, chat_id, folder_name):
    while True:
        for root, dirs, files in os.walk(folder_name):  
            files = files

        random.shuffle(files)

        for filename in files:
            with open(f'{folder_name}/{filename}', 'rb') as document:
                bot.send_document(chat_id=chat_id, document=document)
            time.sleep(frequency*3600)

def main():
    parser_frequency = argparse.ArgumentParser(description='Введите частоту отправки фото в телеграм канал')
    parser_frequency.add_argument("--frequency", help="Введите частоту отправки фото в телеграм канал", default='4', type=int)
    args = parser_frequency.parse_args()
    frequency = args.frequency
    
    load_dotenv()
    folder_name = 'images'
    chat_id = os.environ['CHAT_ID_TELEGRAM']
    bot = telegram.Bot(token=os.environ['TOKEN_TELEGRAM_BOT'])

    try:
        publish_photos(frequency, bot, chat_id, folder_name)
    except telegram.error.InvalidToken:
        print(f'У вас неправильный телеграм токен бота')

if __name__ == "__main__":
    main()