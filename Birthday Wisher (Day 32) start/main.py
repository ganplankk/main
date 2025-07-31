import smtplib
import datetime as dt
from encodings.quopri_codec import quopri_encode
import pandas as pd
import random

my_email = "hs.bang@piolink.com"
password = "xxxx"
now = dt.datetime.now()
week = now.weekday()

if week == 3:
    with open('quotes.txt') as qt:
        # quote_list = [line.strip() for line in qt]
        quote_list = qt.readlines()
        body = random.choice(quote_list)

    with smtplib.SMTP_SSL(host="smtp.dooray.com", port=465) as connection:
        # connection.starttls() 얘는 587 포트 사용
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="fifas9011@gmail.com",
            msg=f"From:hs.bang@piolink.com\nTo:fifas9011@gmail.com\nSubject:Thinking\n\n{body}"
        )

# while True:
#     if week == 0:
#         subject = "hello"
#         body = random.choice(quote_list)
#         messages = f"From: hs.bang@piolink.com\n\nTo: fifas9011@gmail.com\n\nSubject: {subject}\n\n{body}"
#         with smtplib.SMTP_SSL(host="smtp.dooray.com",port=465) as connection:
#             # connection.starttls() 얘는 587 포트 사용
#             connection.login(user=my_email,password=password)
#             connection.sendmail(from_addr=my_email,to_addrs="fifas9011@gmail.com",
#                 # msg = messages
#                 msg = f"From: hs.bang@piolink.com Subject: Hello\n\n{body}")
#         break
#     else:
#         break
# Use the datetime module to obtain the current day of the week.
# Opem the quotes.txt file and obtain a list of quotes.
# Use the random module to pick a random quote from your list of quotes
# Use the smtplib to send the email to yourself.