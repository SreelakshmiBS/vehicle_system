from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import VehicleModel, BookingModel
from .serializers import VehicleSerializer, BookingSerializer

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Vehicle Inventory API</h1><p>API is running successfully.</p>")

class VehicleListCreateView(generics.ListCreateAPIView):

    queryset = VehicleModel.objects.all()

    serializer_class = VehicleSerializer

    filter_backends = [DjangoFilterBackend]

    filterset_fields = [
        "brand",
        "fuel_type",
        "is_available",
    ]


class VehicleDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = VehicleModel.objects.all()

    serializer_class = VehicleSerializer


class BookingListCreateView(generics.ListCreateAPIView):

    queryset = BookingModel.objects.all()

    serializer_class = BookingSerializer


class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = BookingModel.objects.all()

    serializer_class = BookingSerializer