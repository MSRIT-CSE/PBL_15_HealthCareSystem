import smtplib
import serial #Import Serial Library
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sport="com6"
asO=serial.Serial(sport, 9600)

# me == my email address
# you == recipient's email address
me = "my@email.com"
you = "vishwa.kulkarni@gmail.com"
you1 = "vishalmahuli8@gmail.com"
# temp=[];

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Temperature Emergency"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
text = "There's an Emergency, The patient's Body Temperature is going crazy! He needs Help!"
# Record the MIME types of both parts - text/plain and text/html2
part = MIMEText(text, 'plain')

# Attach parts into message container.# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part)
msg1 = MIMEMultipart('alternative')
msg1['Subject'] = "Heart Beat Emergency"
msg1['From'] = me
msg1['To'] = you

# Create the body of the message (a plain-text and an HTML version).
text1 = "There's an Emergency, The patient's Heart Beat is going crazy! He/She needs Help!"
# Record the MIME types of both parts - text/plain and text/html2
part1 = MIMEText(text1, 'plain')

# Attach parts into message container.# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg1.attach(part1)
# Send the message via local SMTP server.
mail = smtplib.SMTP_SSL('smtp.googlemail.com', 465)

mail.ehlo
mail.login('iamyourdoctor134@gmail.com', 'pblproject')
temparature=[]
pulse=[]
while(1==1):
    if(asO.inWaiting()>0):
        temp=asO.readline()
        r=temp.split();
        temparature.append(r[0])
        pulse.append(r[1])
        print temparature
        print pulse
        if(r[0] > 22):
            mail.sendmail(me, you, msg.as_string())
            mail.sendmail(me, you1, msg.as_string())
        if(r[1] >1 and r[1] < 3):
            mail.sendmail(me, you, msg1.as_string())
mail.quit()
