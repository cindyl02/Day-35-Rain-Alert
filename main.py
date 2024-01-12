import requests
import smtplib
from config import API_KEY, MY_EMAIL, MY_PASSWORD

MY_LAT = 49.282730
MY_LONG = -123.120735

ENDPOINT = f"https://api.openweathermap.org/data/2.5/forecast"
weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(url=ENDPOINT, params=weather_params)
response.raise_for_status()
print(response.status_code)
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Rain in the next 12 hours. Bring an umbrella!\n\nIt is raining in the next 12 hours."
        )
    print("Bring an umbrella.")
