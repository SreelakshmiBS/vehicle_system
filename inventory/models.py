from django.db import models

# Create your models here.
class VehicleModel(models.Model):
    name = models.CharField(max_length =100)
    brand = models.CharField(max_length=100)
    year = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=10,decimal_places=2)
    FUEL_CHOICES = [
            ("Petrol", "Petrol"),
            ("Diesel", "Diesel"),
            ("Electric", "Electric"),
            ("Hybrid", "Hybrid"),
        ]
    fuel_type = models.CharField(max_length=100,choices=FUEL_CHOICES)
    is_available = models.BooleanField(default=True)

class BookingModel(models.Model):

    vehicle = models.ForeignKey(
        VehicleModel,
        on_delete=models.CASCADE,
        related_name="bookings"
    )

    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=10)

    start_date = models.DateField()
    end_date = models.DateField()

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    