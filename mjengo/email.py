from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_welcome_email(name, receiver):
    # Creating message subject and sender
    subject = 'Welcome to MJENZI'
    sender = 'mjenziapp@gmail.com'

    # passing in the context variables
    html_content = render_to_string('email/email.html', {"name": name})

    msg = EmailMultiAlternatives(subject, html_content, sender, [receiver])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
