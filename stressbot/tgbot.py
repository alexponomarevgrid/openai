import base64
import telebot
import openai
import logging
import os
import json

FULL_TOKEN = os.getenv("FULL_TOKEN")

FULL_TOKEN_MSG = base64.b64decode(FULL_TOKEN).decode('utf-8')

TOKEN_TG = json.loads(FULL_TOKEN_MSG).get("TOKEN_TG")
TOKEN_AI = json.loads(FULL_TOKEN_MSG).get("TOKEN_AI")
openai.organization = json.loads(FULL_TOKEN_MSG).get("ORGANIZATION")
openai.api_key = TOKEN_AI

bot = telebot.TeleBot(TOKEN_TG, parse_mode=None)

msgArray = []

def chat(msg):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=msg
    )
    return completion


if __name__ == '__main__':

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "Write something and chatGPT will answer you?")

    @bot.message_handler(commands=['history'])
    def send_welcome(message):
        history = ""
        for elem in msgArray:
            history = history + f"{elem.get('role')}: {elem.get('content')}\n"
        bot.reply_to(message, history)

    @bot.message_handler(commands=['clear'])
    def send_welcome(message):
        msgArray.clear()
        bot.reply_to(message, "History was cleaned")

    @bot.message_handler(func=lambda message: True)
    def echo_all(message):
        user_input = message.text

        msgArray.append({"role": "user", "content": user_input})

        answer = chat(msgArray).choices[0].message.content

        msgArray.append({"role": "assistant", "content": answer})

        print(f"{message.from_user.username} write: {message.text} / {answer}")

        bot.reply_to(message, answer)

bot.infinity_polling(logger_level=logging.ERROR)
