from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    steps = models.TextField()
    preparation_time = models.PositiveIntegerField()
    image = models.ImageField(upload_to='recipes/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='recipes')

    def __str__(self):
        return self.name