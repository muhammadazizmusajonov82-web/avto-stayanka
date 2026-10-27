from django.contrib import admin
from .models import CarParking


@admin.register(CarParking)
class CarParkingAdmin(admin.ModelAdmin):
	list_display = ('plate_number', 'car_model', 'arrival_time', 'is_active', 'total_charge')
	list_filter = ('is_active', 'arrival_time')
	search_fields = ('plate_number', 'car_model')
