import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_chatgpt(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Ты туристический помощник. Помогай выбрать тур."},
            {"role": "user", "content": message}
        ]
    )
    return response['choices'][0]['message']['content']
