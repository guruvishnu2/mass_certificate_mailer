# Python code to illustrate Sending mail with attachments 
# from your Gmail account 
# Python program to explain cv2.putText() method 
	
# importing cv2 
import cv2 

	
import csv, smtplib, ssl
import cv2

import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

fromaddr = str(input("EnterSender Mail id:"))
password = str(input("Enter Password:"))

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(fromaddr, password)
    with open("mailids.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for a,email,name in reader:
            text = name
	
# path of the certificate template
	    path = r'C:\Users\padma priya\Desktop\testmailidvision\c.jpg'
	
# Reading an image in default mode 
	    image = cv2.imread(path) 
# font 
            font = cv2.FONT_HERSHEY_SIMPLEX 

# org 
            org = (00, 185) 

# fontScale 
            fontScale = 1

# Red color in BGR 
            color = (0, 0, 255) 

# Line thickness of 2 px 
            thickness = 2

# Using cv2.putText() method 
            image1 = cv2.putText(image, text, org, font, fontScale, color, thickness, cv2.LINE_AA, False) 
            toaddr = email

# instance of MIMEMultipart 
            msg = MIMEMultipart() 

# storing the senders email address 
            msg['From'] = fromaddr 

# storing the receivers email address 
            msg['To'] = email

# storing the subject 
            msg['Subject'] = "Subject of the Mail"

# string to store the body of the mail 
            body = "Body_of_the_mail"

# attach the body with the msg instance 
            msg.attach(MIMEText(body, 'plain')) 

# open the file to be sent 
            attachment = image1

# instance of MIMEBase and named as p 
            p = MIMEBase('application', 'octet-stream') 

# attach the instance 'p' to instance 'msg' 
            msg.attach(p) 

# Converts the Multipart msg into a string 
            text = msg.as_string() 

# sending the mail 
            server.sendmail(fromaddr, toaddr, text) 



