Vehicle Inventory & Booking REST API

The Vehicle Inventory & Booking API is a RESTful web application developed using Django and Django REST Framework (DRF). It enables users to manage vehicle inventory and handle vehicle bookings through secure and well-structured REST APIs. The application follows REST principles and provides complete CRUD (Create, Read, Update, Delete) functionality for both vehicles and bookings.

The system includes real-world business logic to ensure data integrity and prevent invalid bookings. It validates customer phone numbers, prevents bookings with past start dates, ensures the end date is after the start date, prevents overlapping bookings for the same vehicle, automatically calculates the total booking amount based on the rental duration and the vehicle's daily rental price, and marks a vehicle as unavailable once it has been successfully booked.

To improve usability, the API supports filtering of vehicles by brand, fuel type, and availability using django-filter. Interactive API documentation is generated using drf-spectacular (Swagger/OpenAPI), allowing developers to explore and test all endpoints directly from the browser.

Technologies Used
Python
Django
Django REST Framework (DRF)
SQLite
django-filter
drf-spectacular (Swagger/OpenAPI)
Key Features
Vehicle CRUD operations
Booking CRUD operations
Automatic booking amount calculation
Prevention of overlapping bookings
Phone number validation
Date validation
Vehicle availability management
Vehicle filtering (brand, fuel type, availability)
Interactive Swagger API documentation
RESTful API design following best practices
Business Rules
A vehicle cannot be booked for overlapping dates.
The total booking amount is calculated automatically based on the number of rental days and the vehicle's daily rental price.
The booking start date cannot be in the past.
The end date must be later than the start date.
Customer phone numbers must contain exactly 10 digits.
Once a booking is confirmed, the vehicle is marked as unavailable
