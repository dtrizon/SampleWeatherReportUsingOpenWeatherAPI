#https://twitter.com/ngcp_alert
import geocoder
import requests
import json

g = geocoder.ip('me')
lat, lng = g.latlng

api_key = "insert your api key here"
link = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={api_key}&units=metric"
response = requests.get(link).text
response_info = json.loads(response)

country = response_info['sys']['country']
city = response_info['name']
temperature = response_info['main']['temp']
temperature_fl = response_info['main']['feels_like']
humidity = response_info['main']['humidity']
min_temp = response_info['main']['temp_min']
max_temp = response_info['main']['temp_max']

print(f'The country is {country} in the city of {city} with a temp of {temperature}C but feels like {temperature_fl}C. Humidity is {humidity}% with min temp of {min_temp}C and max temp of {max_temp}C.')
