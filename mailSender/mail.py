from email.message import EmailMessage
#from settings import password

from decouple import config
import ssl
import smtplib

#password = config('PASS')

email_sender = 'fbaezahurtado@gmail.com'
email_password = config('PASS')
email_receiver='baezeta@gmail.com'

subject = 'Fernando Baeza from Python'
body="""
Probando un Python script


{
     "name": "Fernando",
     "surname": "Baeza",
     "email": "fbaezahurtado@gmail.com"
}
"""
em= EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['subject']=subject
em.set_content(body)

context= ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())