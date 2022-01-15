#!/usr/bin/python3
# Filename: sendmail.py
# This script is used to send an email from kyle to john.


import smtplib

sender = 'mrj@example.com'
receiver = 'admin@example.com'

message = """From: mrj <mrj@example.com>
To: admin <admin@example.com>
Subject: Test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('127.0.0.1',25)
   smtpObj.ehlo()
   smtpObj.sendmail(sender, receiver, message) 
   print("Successfully sent email")
except SMTPException:
   print("Error: unable to send email")
finally:
   smtpObj.quit()
