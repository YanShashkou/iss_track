import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 50.064651 # Your latitude
MY_LONG = 19.944981 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
print(iss_latitude, iss_longitude)

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

while True:
    if time_now.hour < sunrise or time_now.hour > sunset:
        if MY_LAT-5 < iss_latitude < MY_LAT + 5 and MY_LONG-5 < iss_longitude <MY_LONG+5:
            connection = smtplib.SMTP("smtp.gmail.com", port=587)
            connection.starttls()
            connection.login(user='', password='')
            connection.sendmail(from_addr='', to_addrs="", msg='Look up')
            connection.close()
    time.sleep(60)




