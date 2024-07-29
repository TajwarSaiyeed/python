import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

city = input("Enter city name: ")
url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

r = requests.get(url)
data = json.loads(r.text)
print(data['current']["temp_c"])
say_temp = f'''spd-say "The temperature of {city} is {data['current']['temp_c']} degree celsius"'''
os.system(say_temp)
# print(r.text)
# print(r.json())
