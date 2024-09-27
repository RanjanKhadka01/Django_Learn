from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Recepie(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
  recepie_name = models.CharField(max_length=50)
  receipe_discription = models.TextField(max_length=100)
  receipe_image = models.ImageField(upload_to='receipe')