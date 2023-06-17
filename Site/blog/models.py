from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    #photo = models.ImageField(upload_to="photos/%Y/%m/%d")

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=20)

    def __str__(self):
        return self.name