from django.db import models



# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, default='')
    score = models.DecimalField(max_digits=10 , decimal_places=3)

    def __str__(self):
        return self.name
    