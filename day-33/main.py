import requests
import smtplib
from datetime import datetime
import time

MY_LAT = 37.566536
MY_LONG = 126.977966
DATE = datetime.now()
FORMAT = 0

## SMTP
my_email = "hs.bang@piolink.com"
password = "Piolink.com1@"

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": FORMAT
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    if sunrise > time_now < sunset:
        return True

def is_oss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    iss_position = (longitude, latitude)
    my_position = (MY_LONG, MY_LAT)
    if latitude -5  >= MY_LAT <= latitude +5 and longitude -5 >= MY_LONG <= longitude +5:
        return True

while True:
    time.sleep(60)
    if is_oss_overhead() and is_night():
        with smtplib.SMTP_SSL(host="smtp.dooray.com", port=465) as connection:
            connection.login(user=my_email,password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="fifas9011@gmail.com",
                msg=f"From:hs.bang@piolink.com\nTo:fifas9011@gmail.com\nSubjects=LookUp!\n\nup your neck and see the sky"
            )


#
# if latitude -5  >= MY_LAT <= latitude +5 and longitude -5 >= MY_LONG <= longitude +5:
#     if 24 > time_now < 18:
#         with smtplib.SMTP_SSL(host="smtp.dooray.com", port=465) as connection:
#             connection.login(user=my_email,password=password)
#             connection.sendmail(
#                 from_addr=my_email,
#                 to_addrs="fifas9011@gmail.com",
#                 msg=f"From:hs.bang@piolink.com\nTo:fifas9011@gmail.com\nSubjects=Hello\n\nup your neck and see the sky"
#             )
#

#If the ISS is close to my current

