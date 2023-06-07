import openai
import os
import json

openai.api_key = "sk-FXaflIs8Nb4lwikLwIjiyKZcff1hQNkF6CIxCYghJAIiREXp"
openai.api_base = "https://api.aiproxy.io/v1"


def list_model(file_path="/home/model_list"):
    with open(file_path, "w") as file:
        file.write(json.dumps(openai.Model.list()))


def chat(content, model="gpt-3.5-turbo", role="user", temperature=0):
    completion = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": role,
             "content": content
             }
        ],
        temperature = temperature,
    )
    return completion.choices[0].message.decode("utf-8")

print(chat("告诉我一些特别的VSCode使用技巧"))