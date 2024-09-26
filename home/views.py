from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


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