from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utils import send_email_to_client, send_email_with_attachment
from django.conf import settings

# Create your views here.

def send_email(request):
  subject = 'Email with attachment'
  message = 'Hey find this attach file with this email'
  recipient_list = ['khadkaranjan5@gmail.com']
  file_path = f'{settings.BASE_DIR}/main.txt'
  # send_email_to_client()
  send_email_with_attachment(subject, message, recipient_list, file_path)
  return redirect('/')



def home(request):

  peoples = [
      {'name': 'Ram Khadka', 'age': 25},
      {'name': 'Shyam Sharma', 'age': 15},
      {'name': 'Aakash Giri', 'age': 16},
      {'name': 'Hari Poudel', 'age': 21}
  ]

  text = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Aliquam ipsum suscipit recusandae necessitatibus aperiam doloribus repellat accusantium sint. Totam quae quibusdam et sunt dignissimos placeat dolorum autem omnis mollitia beatae eos eligendi possimus minus sint natus eveniet nulla ipsum ducimus non ullam hic, culpa recusandae neque. Tenetur quam maiores voluptate.'


  return render(request, 'index.html', context={'peoples':peoples, 'text':text})


def contact(request):
  return render(request, 'contact.html')

def about(request):
  return render(request, 'about.html')