# import smtplib
# my_email = "ez"
# password = "***"
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls() #securing connection
# connection.login(user = my_email,password= password)
# connection.sendmail(from_addr=my_email, to_addrs="***", msg="hello")
# connection.close()



import datetime as dt
import random


num = random.randint(0,100)
file = open("day32\quotes.txt")
list = file.readlines()

now =dt.datetime.now()
day =now.weekday()
if day == 6:
    print(list[num])