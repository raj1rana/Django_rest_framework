from django.db import models

# Create your models here
class Autor(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)

class Books(models.Model):
    title = models.CharField(max_length=20)
    ratings = models.CharField(max_length=10)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='books')

