##################### Normal Starting Project ######################
from datetime import datetime
import pandas as pd
import random
import smtplib
## Birthdays
birthdays_file = 'birthdays.csv'
data = pd.read_csv(birthdays_file)

today = datetime.now()
today_tuple = (today.month, today.day)
MY_EMAIL = "hs.bang@piolink.com"
MY_PASSWORD = "Piolink.com1@"

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)

# HINT 2: Use pandas to read the birthdays.csv
# birthday_month = [mon['name'] for mon in birthdays_list if mon['month'] == today_tuple[0]]
# birthday_day = [mon['day'] for mon in birthdays_list if mon['month'] == today_tuple[0]]

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index,data_row) in data.iterrows()}
# print(birthdays_dict)

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        letter = contents.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP_SSL("smtp.dooray.com", port=465) as connection:
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"From:hs.bang@piolink.com\nTo:fifas9011@gmail.com\nSubject:Happy Birthday ~!\n\n{letter}"
                            )

# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
#Dictionary comprehension template for pandas DataFrame looks like this:

#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter. 
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.



