import config
import telebot
import requests
from bs4 import BeautifulSoup as BS

bot = telebot.TeleBot(config.BOT_TOKEN)

@bot.message_handler(commands=['start'])
def main(message):
    text = ''
    r = requests.get('https://sinoptik.ua/погода-москва')
    html = BS(r.content, 'html.parser')
    el = html.select('#content')[0]
    date = el.select('.date')[0].text
    t_min = el.select('.temperature .min')[0].text
    t_max = el.select('.temperature .max')[0].text
    description = el.select('.wDescription .description')[0].text.strip()
    text = f'Погода в Москве. Число сегодня: {date}\nТемпература: {t_min} {t_max}\n{description}'
    
    bot.send_message(message.chat.id, text)
    
bot.polling(none_stop=True)
