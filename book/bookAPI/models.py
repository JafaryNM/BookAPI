from django.db import models
from django.forms import IntegerField

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length = 150)
    published_date=models.DateField()
    quality=models.IntegerField()
    

    def __str__(self):
       return self.title
