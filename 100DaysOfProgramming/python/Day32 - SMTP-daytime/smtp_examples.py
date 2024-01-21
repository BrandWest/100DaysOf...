import smtplib

'''
    Emails
        # temptober@yaoo.com
        # polimer123
        
        # temptober@gmail.com
        # tempTOBER1
'''

gmail = "temptober@gmail.com"
gmail_password = "qgcoxgdjuxillokz"

yahoo = "temptober@yahoo.com"
yahoo_password = ""

protocol_gmail = "smtp.gmail.com"
protocol_yahoo = "smtp.mail.yahool.com"

message = "Subject: My Subject\n\nThis is a message body"

with smtplib.SMTP(protocol_gmail, port=587) as connection_gmail:
    # connection_yahoo = smtplib.SMTP("smtp.mail.yahoo.com")
    connection_gmail.starttls()
    connection_gmail.login(user=gmail, password=gmail_password)

    connection_gmail.sendmail(from_addr=gmail, to_addrs=yahoo, msg=message)


with smtplib.SMTP(protocol_yahoo, port=587) as connection_yahoo:
    connection_yahoo.startls()
    connection_yahoo.login(user=yahoo, password=yahoo_password)

    connection_yahoo.sendmail(from_addr=yahoo, to_addrs=gmail, msg=message)


