from django.db import models

# Create your models here.

class Student(models.Model):
  name = models.CharField(max_length=50)
  age = models.IntegerField()
  email = models.EmailField()
  address = models.TextField(max_length=100)
  # image = models.ImageField(null=True, blank=True)
  # file = models.FileField()



class Car(models.Model):
  name = models.CharField(max_length=100)
  speed = models.IntegerField(default=50)

  def __str__(self):
    return self.name


