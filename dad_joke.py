#!/usr/bin/python3

import requests
import json

def get_joke():
    api_end_point = "https://official-joke-api.appspot.com/jokes/random"
    joke = requests.get(api_end_point)
    json_data = json.loads(joke.text)   
    joke_id = json_data["id"]
    joke_type = json_data["type"]
    joke_setup = json_data["setup"]
    joke_punchline = json_data["punchline"]
    print(joke_id)
    print(joke_type)
    print(joke_setup)
    print(joke_punchline)


if __name__ == "__main__":
    get_joke()