from django.contrib import admin
from flightapp.models import (Flight,Reservation,Passanger)
# Register your models here.
admin.site.register(Flight)
admin.site.register(Reservation)
admin.site.register(Passanger)