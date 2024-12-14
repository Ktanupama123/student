from django.db import models 

# Create your models here.
class Student(models.Model):
    name= models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    email=models.EmailField(unique=True)


    def __str__(self):
        return self.name