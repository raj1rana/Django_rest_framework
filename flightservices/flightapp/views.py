from flightapp.models import(Flight,Passanger,Reservation)
from flightapp.serializers import(FlightSerializer, PassangerSerializer, ReservationSerializer)
from rest_framework import viewsets
# Create your views here.
class FlightViewSets(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    
class PassangerViewSets(viewsets.ModelViewSet):
    queryset = Passanger.objects.all()
    serializer_class = PassangerSerializer
class ReservationViewSets(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer 