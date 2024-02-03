from django.db import models
#from .models import Member

# Create your models here.


class Member(models.Model):
    firstname=models.CharField(max_length=150)
    lastname=models.CharField(max_length=150)
    country=models.CharField(max_length=150)
