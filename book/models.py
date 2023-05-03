from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    publication_date = models.DateField(auto_now_add=True)
    isbn = models.BigIntegerField(unique=True, blank=True, null=True, validators=[MinValueValidator(100000000000,message='ISBN must be a 13-digit number.'),MaxValueValidator(9999999999999,message='ISBN must be a 13-digit number.') ])
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title
