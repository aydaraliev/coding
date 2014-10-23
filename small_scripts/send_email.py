#!/home/laba/anaconda/bin/python

import smtplib
import datetime
import email.utils
from email.mime.text import MIMEText

fromaddr = 'yourprocessisdone@gmail.com'
toaddr = 'aidaraliev@gmail.com'
msg = MIMEText('Overlord, I have completed the task you gave me at %s' % datetime.datetime.now())
msg['Subject'] = 'Notification on task completion'

username = 'yourprocessisdone'
password = 'qazqazqazqaz'

server = smtplib.SMTP('smtp.gmail.com:587')

server.starttls()

server.login(username, password)

server.sendmail(fromaddr, [toaddr], msg.as_string())

server.quit()
