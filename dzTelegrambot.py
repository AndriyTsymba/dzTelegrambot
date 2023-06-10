import telebot
from telebot import types
import wikipedia
import requests

bot = telebot.TeleBot('6268151355:AAEG_h_DRFDsAInnc1LVfRDrs2tTyGJaYhI')
@bot.message_handler(commands=['start'])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Напишіть назву статті:')
@bot.message_handler(content_types=['text'])
def handler_text(message):
    name = message.text
    wikipedia.set_lang("uk")
    response = requests.get('https://uk.wikipedia.org/wiki/' + name)
    if response.status_code == 200:
        if wikipedia.summary(name, chars=1000):
            answer = f"Інфа, яку вдалося знайти:\n\n" \
                     f"{'https://uk.wikipedia.org/wiki/' + name}\n\n" \
                     f"{wikipedia.summary(name, chars=1000)}\n\nПродовження тут:\n\n" \
                     f"{'https://uk.wikipedia.org/wiki/' + name}"

        else:
            answer = 'Щось пішло не так ('
    else:
        answer = f'Статті з назвою "{name}" не знайдено.'
    bot.send_message(message.chat.id, answer)

bot.polling()