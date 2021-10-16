from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name, receiver):
    #creating mesage subject and sender
    subject="Welcome To InstagramClone"
    sender='Testshelly29@gmail.com'

    #passing context variables
    text_context=render_to_string('email/welcome.txt',{"name":name})
    html_content=render_to_string('email/welcome.html',{"name":name})

    msg =EmailMultiAlternatives(subject,text_context,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')

    msg.send()
