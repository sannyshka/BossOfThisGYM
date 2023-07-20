from django.db import models
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title