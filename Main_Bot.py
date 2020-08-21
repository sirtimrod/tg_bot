import datetime
import schedule
import telebot
import time

bot = telebot.TeleBot('ENTER YOUR TELEGRAM TOKEN')
now = datetime.datetime.now()
hour = now.hour
chat_id = None
name_of_crush = None

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hi, please tell me your boyfriend's name")

@bot.message_handler(content_types=['text'])
def get_chat_informathion(message):
    global name_of_crush
    global chat_id
    global hour
    chat_id = message.chat.id
    name_of_crush = message.text
    bot.send_message(chat_id, f'{name_of_crush} - cool name\n'
                              f'OK, now wait for messages from your crush')
    everyday_sending()

def everyday_sending():
    schedule.every().day.at("YOUR TIME").do(send_morning_text)
    schedule.every().day.at("YOUR TIME").do(send_afternoon_text)
    schedule.every().day.at("YOUR TIME").do(send_evening_text)
    while True:
        schedule.run_pending()
        time.sleep(1)

def send_morning_text():
    bot.send_message(chat_id, f'Good morning, sweetheart \U0001F618'
                              f'\n{name_of_crush} loves you and wishes you a good day \u2764\ufe0f')

def send_afternoon_text():
    bot.send_message(chat_id, f'Good afternoon, honey \U0001F60D'
                              f'\n{name_of_crush} still loves you and conveys that you are perfect \U0001F337')

def send_evening_text():
    bot.send_message(chat_id, f'Good evening, princess \U0001F496'
                              f'\n{name_of_crush} loves you more than anyone else and wishes you sweet dreams \U0001F48F')

bot.polling(none_stop=True)
