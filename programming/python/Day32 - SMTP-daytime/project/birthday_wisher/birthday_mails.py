import smtplib
from email.utils import formataddr
from email.message import EmailMessage
from modules.birthdays import Birthday
from random import randint

def check_birthdays():
    for name in birthday.birthday_dict:
        email = birthday.birthday_dict[name]["email"]
        
        if birthday.birthday_dict[name]["year"] == birthday.now.year:
            send_mail(name, email)
        
        else:
            # send_mail(name, email)
            if name == "Debbie":
                send_mail(name, email)


def send_mail(name, email):
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



if __name__ == "__main__":
    birthday = Birthday()
    birthday.open_birthday_list()
    birthday.get_datetime()
    birthday.get_paramters()
    check_birthdays()

