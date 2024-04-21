from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    detail = models.TextField(blank=True, null=True, max_length=1000)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list')