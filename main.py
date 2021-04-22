import requests
import os
from twilio.rest import Client

MY_LAT = 42.084363  #50.843788
MY_LONG = 19.096714 #4.488360
API_KEY = "dbe244c47c786cfa985480e881f15862"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "AC3527f8c0f1d47acd942a3e2eaa3b2266"
auth_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude":"current,minutely,daily",
}

# api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

# http://api.openweathermap.org/data/2.5/weather?q=Brussels,BE&appid=dbe244c47c786cfa985480e881f15862
# https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}


response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
print(weather_slice)

condition_list = []
will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) <= 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Python Twilio weather SMS test!",
        from_="+18602003804",
        to="+32486226706"
    )
    print(message.status)

# twilio Your new Phone Number is +18602003804

#     id_list.append(condition_code)
# print(id_list)


