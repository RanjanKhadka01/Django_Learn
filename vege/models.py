from django.db import models

# Create your models here.


class Recepie(models.Model):
  recepie_name = models.CharField(max_length=50)
  receipe_discription = models.TextField(max_length=100)
  receipe_image = models.ImageField(upload_to='receipe')