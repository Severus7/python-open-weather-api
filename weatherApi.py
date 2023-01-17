import datetime as dt
import requests
import pandas as pd
from IPython.display import display
import csv

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "405af6a3d70c1a804713877c3eceb864"
CITY = "Marikina"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

print(response)