from rest_framework import serializers
from flightapp.models import (Passanger, Flight, Reservation)

class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight
        fields = '__all__'

class PassangerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Passanger
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = '__all__'