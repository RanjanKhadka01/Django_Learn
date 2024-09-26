from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


# Create your views here.

def receipe(request):
  if request.method == 'POST':
    data = request.POST

    receipe_name = data.get('receipe_name')
    receipe_description = data.get('receipe_description')
    receipe_image = request.FILES.get('receipe_image')

    Recepie.objects.create(
      recepie_name = receipe_name,
      receipe_discription = receipe_description,
      receipe_image = receipe_image
    )
    return redirect('/receipe/')
  
  queryset = Recepie.objects.all()

  # For Search
  if request.GET.get('search'):
    queryset = queryset.filter(recepie_name__icontains = request.GET.get('search'))


  context = {'receipes': queryset}

  return render(request, 'receipe.html', context)


def update_receipe(request, id):
  queryset = Recepie.objects.get(id = id)
  if request.method == 'POST':
    data = request.POST

    receipe_name = data.get('receipe_name')
    receipe_description = data.get('receipe_description')
    receipe_image = request.FILES.get('receipe_image')


    queryset.recepie_name = receipe_name
    queryset.receipe_discription = receipe_description

    if receipe_image:
      queryset.receipe_image = receipe_image
    queryset.save()
    
    return redirect('/receipe/')
  context = {'receipe': queryset}
  return render(request, 'update_receipe.html', context)


def delete_receipe(request, id):
  queryset = Recepie.objects.get(id = id)
  queryset.delete()
  return redirect('/receipe/')
  