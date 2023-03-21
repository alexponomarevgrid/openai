import openai
import os
import json
import base64

FULL_TOKEN = os.getenv("FULL_TOKEN")

FULL_TOKEN_MSG = base64.b64decode(FULL_TOKEN).decode('utf-8')

TOKEN_AI = json.loads(FULL_TOKEN_MSG).get("TOKEN_AI")
openai.organization = json.loads(FULL_TOKEN_MSG).get("ORGANIZATION")
openai.api_key = TOKEN_AI


def chat(msg):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=msg
    )
    return completion


if __name__ == '__main__':

    msg = []
    while True:
        user_input = input("You: ")

        print(msg)
        if len(msg) < 1:
            msg = [{"role": "user", "content": user_input}]
        else:
            msg.append({"role": "user", "content": user_input})
        print(msg)
        response = chat(msg)
        answer = response.choices[0].message.content.replace("\n\n", "\n")

        msg.append({"role": "assistant", "content": answer})
        print(msg)

        print(f"AI: {answer}")

    # r = openai.Image.create(
    #     prompt="Pepe of mankind",
    #     n=2,
    #     size="1024x1024"
    # )
    #
    # print(r)