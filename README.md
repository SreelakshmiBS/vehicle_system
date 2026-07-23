# Vehicle Inventory & Booking REST API

A RESTful API built using **Django** and **Django REST Framework (DRF)** for managing vehicle inventory and vehicle bookings. The application provides complete CRUD (Create, Read, Update, Delete) operations for vehicles and bookings, supports filtering, validates booking requests, prevents double bookings, and automatically calculates booking charges.

---

# Live Deployment

### Live Application

https://vehicle-system-2ipa.onrender.com/

### Swagger API Documentation

https://vehicle-system-2ipa.onrender.com/api/docs/

### OpenAPI Schema

https://vehicle-system-2ipa.onrender.com/api/schema/

### GitHub Repository

https://github.com/SreelakshmiBS/vehicle_system

---

# Features

- Vehicle CRUD Operations
- Booking CRUD Operations
- Vehicle Filtering
- Automatic Total Amount Calculation
- Phone Number Validation
- Booking Date Validation
- Prevent Double Booking
- Vehicle Availability Management
- Interactive Swagger Documentation
- RESTful API Design
- Render Deployment

---

# Technologies Used

- Python 3
- Django
- Django REST Framework (DRF)
- SQLite
- django-filter
- drf-spectacular (Swagger/OpenAPI)
- Gunicorn
- WhiteNoise
- Render

---

# Project Structure

```
vehicle_system/
│
├── inventory/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── vehicle_system/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── manage.py
├── requirements.txt
├── build.sh
├── .gitignore
└── README.md
```

---

# Setup Steps

## Clone the Repository

```bash
git clone https://github.com/SreelakshmiBS/vehicle_system.git
```

Navigate into the project directory

```bash
cd vehicle_system
```

---

## Create a Virtual Environment

Windows

```bash
python -m venv venv
```

Linux/macOS

```bash
python3 -m venv venv
```

---

## Activate the Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

---

# Installation Guide

Install all dependencies

```bash
pip install -r requirements.txt
```

---

# Migration Commands

Create migration files

```bash
python manage.py makemigrations
```

Apply migrations

```bash
python manage.py migrate
```

(Optional) Create a superuser

```bash
python manage.py createsuperuser
```

---

# Run the Project Locally

Start the Django development server

```bash
python manage.py runserver
```

Open

Home

```
http://127.0.0.1:8000/
```

Swagger Documentation

```
http://127.0.0.1:8000/api/docs/
```

Admin Panel

```
http://127.0.0.1:8000/admin/
```

---

# Live Project Links

| Resource | URL |
|----------|-----|
| Live Application | https://vehicle-system-2ipa.onrender.com/ |
| Swagger UI | https://vehicle-system-2ipa.onrender.com/api/docs/ |
| OpenAPI Schema | https://vehicle-system-2ipa.onrender.com/api/schema/ |
| Vehicles API | https://vehicle-system-2ipa.onrender.com/api/vehicles/ |
| Bookings API | https://vehicle-system-2ipa.onrender.com/api/bookings/ |
| GitHub Repository | https://github.com/SreelakshmiBS/vehicle_system |

---

# How to Test the APIs

You can test the APIs using

- Swagger UI
- Postman
- Thunder Client
- Insomnia

Swagger Documentation

https://vehicle-system-2ipa.onrender.com/api/docs/

---

# API Endpoint List

## Vehicle APIs

### Get All Vehicles

**GET**

```
https://vehicle-system-2ipa.onrender.com/api/vehicles/
```

---

### Create Vehicle

**POST**

```
https://vehicle-system-2ipa.onrender.com/api/vehicles/
```

---

### Retrieve Vehicle

**GET**

```
https://vehicle-system-2ipa.onrender.com/api/vehicles/{id}/
```

Example

```
https://vehicle-system-2ipa.onrender.com/api/vehicles/1/
```

---

### Update Vehicle

**PUT**

```
https://vehicle-system-2ipa.onrender.com/api/vehicles/{id}/
```

---

### Partial Update Vehicle

**PATCH**

```
https://vehicle-system-2ipa.onrender.com/api/vehicles/{id}/
```

---

### Delete Vehicle

**DELETE**

```
https://vehicle-system-2ipa.onrender.com/api/vehicles/{id}/
```

---

## Booking APIs

### Get All Bookings

**GET**

```
https://vehicle-system-2ipa.onrender.com/api/bookings/
```

---

### Create Booking

**POST**

```
https://vehicle-system-2ipa.onrender.com/api/bookings/
```

---

### Retrieve Booking

**GET**

```
https://vehicle-system-2ipa.onrender.com/api/bookings/{id}/
```

Example

```
https://vehicle-system-2ipa.onrender.com/api/bookings/1/
```

---

### Update Booking

**PUT**

```
https://vehicle-system-2ipa.onrender.com/api/bookings/{id}/
```

---

### Partial Update Booking

**PATCH**

```
https://vehicle-system-2ipa.onrender.com/api/bookings/{id}/
```

---

### Delete Booking

**DELETE**

```
https://vehicle-system-2ipa.onrender.com/api/bookings/{id}/
```

---

# Vehicle Filtering

## Filter by Brand

```
GET https://vehicle-system-2ipa.onrender.com/api/vehicles/?brand=Tata
```

---

## Filter by Fuel Type

```
GET https://vehicle-system-2ipa.onrender.com/api/vehicles/?fuel_type=Petrol
```

---

## Filter by Availability

```
GET https://vehicle-system-2ipa.onrender.com/api/vehicles/?is_available=True
```

---

## Multiple Filters

```
GET https://vehicle-system-2ipa.onrender.com/api/vehicles/?brand=Tata&fuel_type=Petrol&is_available=True
```

---

# Sample JSON

## Create Vehicle

```json
{
    "name": "Nexon",
    "brand": "Tata",
    "year": 2025,
    "price_per_day": "1800.00",
    "fuel_type": "Petrol",
    "is_available": true
}
```

---

## Create Booking

```json
{
    "vehicle": 1,
    "customer_name": "Rahul",
    "customer_phone": "9876543210",
    "start_date": "2026-07-25",
    "end_date": "2026-07-28"
}
```

---

## Booking Response

```json
{
    "id": 1,
    "vehicle": 1,
    "customer_name": "Rahul",
    "customer_phone": "9876543210",
    "start_date": "2026-07-25",
    "end_date": "2026-07-28",
    "total_amount": "5400.00"
}
```

---

# Business Rules

- A vehicle cannot be booked for overlapping dates.
- Booking start date cannot be in the past.
- Booking end date must be after the start date.
- Customer phone number must contain exactly 10 digits.
- The total booking amount is calculated automatically.

```
Total Amount = Number of Days × Price Per Day
```

- After a successful booking, the selected vehicle is automatically marked as unavailable.

---

# Deployment

The project is deployed on **Render**.

## Build Command

```bash
./build.sh
```

## Start Command

```bash
gunicorn vehicle_system.wsgi:application
```

---

# Deployment URLs

| Service | URL |
|----------|-----|
| Live Application | https://vehicle-system-2ipa.onrender.com/ |
| Swagger Documentation | https://vehicle-system-2ipa.onrender.com/api/docs/ |
| OpenAPI Schema | https://vehicle-system-2ipa.onrender.com/api/schema/ |
| Vehicle API | https://vehicle-system-2ipa.onrender.com/api/vehicles/ |
| Booking API | https://vehicle-system-2ipa.onrender.com/api/bookings/ |

---

# Author

**Sreelakshmi B S**

Python Developer | Django Developer | Django REST Framework Developer

GitHub: https://github.com/SreelakshmiBS/vehicle_system