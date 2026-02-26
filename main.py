import requests
api_key = "30be9d6f81ee076d9023bf7273f7e725"
lit_lat = "39.604652"
lit_lon = "-105.123779"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
going_to_rain = False

response = requests.get(OWM_Endpoint, params={'lat': lit_lat, 'lon': lit_lon, 'appid': api_key, 'cnt': "4"})
response.raise_for_status()
weather_data = response.json()['list'][0]['weather'][0]['id']



for x in range(0,4):
    print(response.json()['list'][x]['weather'][0]['id'])
    if int(response.json()['list'][x]['weather'][0]['id']) < 700:
        going_to_rain = True


if going_to_rain:
    print("Bring an Umbrella!")
else:
    print("Not going to rain")

