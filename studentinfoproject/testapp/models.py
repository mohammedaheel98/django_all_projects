from django.db import models

# Create your models here.
class Student(models.Model):
    rollno = models.IntegerField()
    name = models.CharField(max_length=30)
    dob = models.DateField()
    email = models.EmailField()
    mark = models.IntegerField()
    phoneno = models.IntegerField()
    address = models.TextField()