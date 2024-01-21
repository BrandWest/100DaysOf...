from random import randint
from email.utils import formataddr
from email.message import EmailMessage
import datetime as dt

import smtplib

def get_file():
    quote = []
    with open ("/home/caboose/codingProjects/python/udemy/Day32 - SMTP-daytime/project/motivation/quotes.txt", "r") as quotes:
         for line in quotes:
              quote.append(line)
    return quote


def get_quotes(quotes):
    index = randint(0, len(quotes)-1)
    return quotes[index]


def send_mail(quote):
    quote, name = quote.split('-')
    name = name.strip()

    gmail = "temptober@gmail.com"
    gmail_password = "qgcoxgdjuxillokz"
    # yahoo = "temptober@yahoo.com"
    yahoo = "debsdsouza8@gmail.com"
    protocol_gmail = "smtp.gmail.com"

    message = EmailMessage()
    message['From'] = formataddr((f"{name}", gmail))
    message['To'] = formataddr(("Debbie",yahoo))
    message['Subject'] = "A motivational quote for you"

    message.set_content(f"{quote}.\n\nSincerly,\n\n{name}")

    with smtplib.SMTP(protocol_gmail, port=587) as connection_gmail:
        connection_gmail.starttls()
        connection_gmail.login(user=gmail, password=gmail_password)
        connection_gmail.send_message(message)



def main():
    quotes = get_file()    
    quote = get_quotes(quotes)
    now = dt.datetime.now()
    #0 = Monday
    if now.weekday() != today:
        send_mail(quote)

    today = now.weekday()

if __name__ == "__main__":
    main()