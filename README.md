## Rain Alert (Day 35)

### About
This project uses the Open Weather API to look at the next 12 hours weather forecast in your location.
If it rains, it will use the email address provided to send an email. 

### How to setup the project
1. Create an account in Open Weather.
2. Use the API key from your account and add it to `config.py` under `API_KEY`.
3. Add your email address and smtp App Password in `config.py` under `MY_EMAIL` and `MY_PASSWORD`.
3. Update MY_LAT and MY_LONG with your location using latlong.net.
4. Use pythonanywhere to continuously run the program by setting up a daily recurring task. 
