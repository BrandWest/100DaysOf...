'''
    What excercise did you do?
        input form user
            date, time, exercises, duration, calories

    input into googlesheets

    NutritionIX
        application ID: cfaf049d
        apikey: a442445984d75b3df25934f3b6933b2a—
        
'''
import requests
import datetime as dt

APP_ID = "cfaf049d"
API_KEY = "7776bf013aa21e3c3bd2543e5f9a899d"
SHEETY_AUTH_KEY = "oUNhSRy5DTpg3yJrX_n"


def process_input():
    tld_nutritionix = "https://trackapi.nutritionix.com/v2/"
    endpoint = "natural/exercise"
    url = f"{tld_nutritionix}{endpoint}"
    headers = {
        "x-app-id" : APP_ID,
        "x-app-key" : API_KEY
    }

    params = {
        "query" : user_input,
    }

    response = requests.post(url=url, headers=headers, json=params)

    return response.json()


def add_data(response):
    tld_post = "https://api.sheety.co/c0600a54c4a69fa054eec83059d2ab39/excerciseTracker/sheet1"
    headers = {
        "Authorization" : f"Bearer {SHEETY_AUTH_KEY}"
    }

    date = str(dt.datetime.today().strftime('%Y-%m-%d'))
    time = str(dt.datetime.now().strftime('%H:%M:%S'))

    for ex in response["exercises"]:
        data = {
            "sheet1" : {
                "date" : date,
                "time" : time,
                "excercise" : ex["name"],
                "duration" : ex["duration_min"],
                "calories" : ex["nf_calories"]
            }
        }
        response_post = requests.post(url=tld_post, headers=headers, json=data)
        response_post.raise_for_status
    

if __name__ == "__main__":
    user_input = input("Please describe the excercise performed: ")
    response = process_input()
    add_data(response)
