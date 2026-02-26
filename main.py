import requests
api_key = "30be9d6f81ee076d9023bf7273f7e725"
lit_lat = "39.604652"
lit_lon = "-105.123779"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(OWM_Endpoint, params={'lat': lit_lat, 'lon': lit_lon, 'appid': api_key})
print(response.json())