from django.db import models
from django.urls import reverse


# Create your models here.
class Post(models.Model):
     title = models.CharField(max_length=255)
     text = models.TextField()
     p = models.ForeignKey('Pl', on_delete=models.PROTECT, null=True, blank=True)
     image = models.ImageField(upload_to='photos/%Y/%m/%d', null=True, blank=True)
     category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
     
     def __str__(self):
          return self.title

     def get_absolute_url(self):
          return reverse('home')

class Category(models.Model):
     name = models.CharField(max_length=255)

     def __str__(self):
          return self.name
     
class P1(models.Model):
     name = models.CharField(max_length=255)