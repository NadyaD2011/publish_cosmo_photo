import telegram

chat_id = '@epic_photo_nasa_spacex'
bot = telegram.Bot(token='7020625424:AAFbZ-VP81FKchx7yJezMZy7odYsSKvYYVg')
bot.send_message(chat_id=chat_id, text="I'm sorry Dave I'm afraid I can't do that.")
bot.send_document(chat_id=chat_id, document='https://gas-kvas.com/grafic/uploads/posts/2024-01/gas-kvas-com-p-chernii-kvadrat-oboi-s-nadpisyu-17.jpg')
