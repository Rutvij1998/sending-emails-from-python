'''
created by Rutvij Kulkarni

'''

import smtplib
import csv
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

fp = input("Enter the file name you want to send with extension\n")
From = input("Enter your Google mail id\n")
your_pass = input("Enter your password\n")
email_data = csv.reader(open('info_list.csv', 'r'))
for row in email_data:
	to = row[1]
	body = "Hello,this is to verify that mail has been sent using a python program"
	subject = input("Enter the subject\n")
	message = MIMEMultipart()
	message['From'] = From
	message['To'] = to
	message['Subject'] = subject
	message.attach(MIMEText(body, fp))
	text = message.as_string()

	mail = smtplib.SMTP('smtp.gmail.com', 587)
	mail.ehlo()
	mail.starttls()
	mail.login(From,your_pass)
	mail.sendmail(From,to, text)
	mail.close()
	print('Mail had been sent succesfully')
