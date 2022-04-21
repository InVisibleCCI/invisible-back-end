from django.core.mail import send_mail
from django.template.loader import render_to_string

from invisible_backend import settings


def send(subject, recipients, message):
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, "", email_from, recipients, html_message=message)


def send_registration_mail(user):
    msg_html = render_to_string('register.html', {'name': user['first_name'], 'id': ['id']})
    subject = 'InVisible vous remercie de votre inscription à notre site'
    recipients = [user['email'], ]
    return send(subject, recipients, msg_html)


def send_reset_password_mail(user, subject, temporary_password, change_password=True):
    msg_html = render_to_string('reset_password.html', {'name': user.first_name,
                                                        'temporary_password': temporary_password,
                                                        'security_mail_token': user.reset_password_token,
                                                        'change_password': change_password})
    recipients = [user.email, ]
    return send(subject, recipients, msg_html)
