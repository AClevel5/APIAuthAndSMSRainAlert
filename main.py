import requests
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Join Earth's mightiest heroes. Like Kevin Bacon.",
    from_="+15017122661",
    to="+15558675310",
)

print(message.body)

api_key = os.environ.get("API_KEY")
lit_lat = "39.604652"
lit_lon = "-105.123779"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
going_to_rain = False

response = requests.get(OWM_Endpoint, params={'lat': lit_lat, 'lon': lit_lon, 'appid': api_key, 'cnt': "4"})
response.raise_for_status()
weather_data = response.json()['list'][0]['weather'][0]['id']



for x in range(0,4):
    print(response.json()['list'][x]['weather'][0]['main'])
    if int(response.json()['list'][x]['weather'][0]['id']) < 700:
        going_to_rain = True


if going_to_rain:
    print("Bring an Umbrella!")
else:
    print("Not going to rain")

