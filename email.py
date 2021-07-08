import smtplib
conn = smtplib.SMTP('imap.gmail.com',587)
conn.ehlo()
conn.starttls()
# below are your credentials. Incorrect credentials will throw an exception which is not handled .
mymail=input("enter your email idrar  ")
password=input("Enter Your Password  ")
sender=input("Enter Receiver's Email ID  ")
Subject=input("Enter Your Subject  ")
Text=input("Enter Text to send  ")
message = 'Subject: {}\n\n{}'.format(Subject, Text)

conn.login(mymail, password) # It will try to login with these Credentials.
conn.sendmail(mymail,sender,message) # It will send Mail.

conn.quit()