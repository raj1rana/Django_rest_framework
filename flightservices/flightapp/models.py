from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.
class Flight(models.Model):
    flightNumber = models.CharField(max_length=10)
    operatingAirlines = models.CharField(max_length=20)
    departureCity = models.CharField(max_length=20)
    arrivalCity = models.CharField(max_length=20)
    dateOfDeparture = models.DateField()
    estimatedTimeOfDeparture = models.TimeField()

    def __str__(self):
        return self.flightNumber
    

class Passanger(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    middleName = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.email
    

class Reservation(models.Model):
    flight = models.OneToOneField(Flight,  on_delete=models.CASCADE)
    passanger = models.OneToOneField(Passanger,  on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def crete_auth_token(sender, instance=None, created=False,  **kwargs):
    if created:
        Token.objects.create(user=instance)