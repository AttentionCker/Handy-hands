import requests
import sys

api_key = 'vEmLU3bpNq7poVGFy4YYgUXVhKw48YSN'

def get_weather(location):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(location, api_key)
    response = requests.get(url)
    return response.json()
