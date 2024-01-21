import requests
from datetime import datetime
import smtplib
from time import sleep
from math import floor


while True:
    MY_LAT = 43.874168 # Your latitude
    MY_LONG = -79.258743 # Your longitude

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

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

    #If the ISS is close to my current position
    # and it is currently dark
    # Then send me an email to tell me to look up.
    # BONUS: run the code every 60 seconds.
    print(time_now, sunrise, sunset)
    iss_latitude = floor(iss_latitude)
    iss_longitude = floor(iss_longitude)

    if iss_longitude + 5 >= int(MY_LONG) or iss_longitude -5 <= int(MY_LONG):
        if iss_latitude + 5 >= int(MY_LONG) or iss_longitude -5 <= int(MY_LONG):
            gmail = "temptober@gmail.com"
            gmail_password = "qgcoxgdjuxillokz"

            protocol_gmail = "smtp.gmail.com"

            message = EmailMessage()
            message['From'] = formataddr((f"Brandon", gmail))
            message['To'] = formataddr((name,email))
            message['Subject'] = "Happy Birthday"

            letter_number = randint(1,3)
            msg = ""
            with open(fr'/home/caboose/codingProjects/python/udemy/Day32 - SMTP-daytime/project/birthday_wisher/template/letter_{letter_number}.txt', 'r') as letter:
                for line in letter:
                    if "[NAME]" in line:
                        msg += line.replace("[NAME]", name)
                    else:
                        msg += line

            message.set_content(f"{msg}")

            with smtplib.SMTP(protocol_gmail, port=587) as connection_gmail:
                connection_gmail.starttls()
                connection_gmail.login(user=gmail, password=gmail_password)
                connection_gmail.send_message(message)


    # sleep(5)


