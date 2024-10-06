from home.models import Student
import time
from django.core.mail import send_mail, EmailMessage
from django.conf import settings


def run_this_function():
  print("Functio started")
  print("Functio started..")

  time.sleep(2)
  print("Function Executed")


def send_email_to_client():
  subject = 'This email is from django server'
  message = 'This is a test message from django server email'
  from_email = settings.EMAIL_HOST_USER
  recipient_list = ['khadkaranjan5@gmail.com']
  send_mail(subject, message, from_email, recipient_list)


def send_email_with_attachment(subject, message, recipient_list, file_path):
  mail = EmailMessage(subject = subject, body = message, from_email = settings.EMAIL_HOST_USER,
                      to = recipient_list)
  mail.attach_file(file_path)
  mail.send()

  