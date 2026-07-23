from datetime import date

from rest_framework import serializers

from .models import VehicleModel, BookingModel


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingModel
        fields = "__all__"
        read_only_fields = ["total_amount"]

    # Validate phone number
    def validate_customer_phone(self, value):
        if not value.isdigit():
            raise serializers.ValidationError(
                "Phone number should contain only digits."
            )

        if len(value) != 10:
            raise serializers.ValidationError(
                "Phone number must contain exactly 10 digits."
            )

        return value

    # Validate all booking details
    def validate(self, attrs):

        vehicle = attrs["vehicle"]
        start_date = attrs["start_date"]
        end_date = attrs["end_date"]

        # Start date cannot be in the past
        if start_date < date.today():
            raise serializers.ValidationError(
                "Start date cannot be in the past."
            )

        # End date must be after start date
        if end_date <= start_date:
            raise serializers.ValidationError(
                "End date must be after the start date."
            )

        # Prevent double booking
        booking_exists = BookingModel.objects.filter(
            vehicle=vehicle,
            start_date__lte=end_date,
            end_date__gte=start_date
        ).exists()

        if booking_exists:
            raise serializers.ValidationError(
                "Vehicle is already booked for the selected dates."
            )

        return attrs

    # Create booking
    def create(self, validated_data):

        vehicle = validated_data["vehicle"]

        start_date = validated_data["start_date"]
        end_date = validated_data["end_date"]

        # Calculate number of days
        total_days = (end_date - start_date).days

        # Calculate total amount
        validated_data["total_amount"] = (
            total_days * vehicle.price_per_day
        )

        # Save booking
        booking = BookingModel.objects.create(**validated_data)

        # Mark vehicle unavailable
        vehicle.is_available = False
        vehicle.save()

        return booking