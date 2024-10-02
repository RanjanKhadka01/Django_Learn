from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator



# Create your views here.
@login_required(login_url='/login/')
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


@login_required(login_url='/login/')
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


@login_required(login_url='/login/')
def delete_receipe(request, id):
  queryset = Recepie.objects.get(id = id)
  queryset.delete()
  return redirect('/receipe/')
  


def register(request):
  if request.method == 'POST':
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = User.objects.filter(username = username)

    if user.exists():
      messages.error(request, "Username already exists..")
      return redirect('/register/')

    user = User.objects.create(
      first_name = first_name,
      last_name = last_name,
      username = username
    )
    user.set_password(password)
    user.save()
    messages.error(request, "Account Created Successfully..")

    return redirect('/register/')

  return render(request, 'register.html')


def login_page(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    if not User.objects.filter(username = username).exists():
      messages.error(request, "Invalid Username")
      return redirect('/login/')
    
    user = authenticate(username = username, password = password)

    if user is None:
      messages.error(request, "Invalid Password")
      return redirect('/login/')
    else:
      login(request, user)
      return redirect('/receipe/')

  return render(request, 'login.html')


def logout_page(request):
  logout(request)
  return redirect('/login')


from django.db.models import Q, Sum

def get_student(request):
  queryset = Student.objects.all()

  if request.GET.get('search'):
    search = request.GET.get('search')
    queryset = queryset.filter(
      Q(student_name__icontains = search) |
      Q(department__department__icontains = search) |
      Q(student_id__student_id__icontains = search) |
      Q(student_email__icontains = search) | 
      Q(student_age__icontains = search)  
    )


  paginator = Paginator(queryset, 5)  # Show 5 contacts per page.

  page_number = request.GET.get("page")
  page_obj = paginator.get_page(page_number)
  print(page_obj)
  return render(request, 'report/student.html', context={'queryset': page_obj})


def see_marks(request, student_id):
  queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id)
  total_marks = queryset.aggregate(total_marks=Sum('marks'))
  return render(request, 'report/see_marks.html', context={'queryset': queryset, 'total_marks': total_marks})
