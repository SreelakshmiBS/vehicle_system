from django.contrib import admin

# Register your models here.
from .models import VehicleModel,BookingModel

admin.site.register(VehicleModel)
admin.site.register(BookingModel)