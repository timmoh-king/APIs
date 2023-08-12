#!/usr/bin/python3

import requests
import json

def get_joke_by_category(category):
    api_end_point = "https://official-joke-api.appspot.com/jokes/"+category+"/random"
    joke = requests.get(api_end_point)
    json_data = json.loads(joke.text)
    joke_setup = json_data[0]["setup"]
    joke_punchline = json_data[0]["punchline"]
    print(joke_setup)
    print(joke_punchline)


if __name__ == "__main__":
    get_joke_by_category("programming")
