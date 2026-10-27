from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import CarParking
from django.db import models
from django.urls import reverse



# 1. Admin uchun registratsiya qismi
def register_admin(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Ro'yxatdan o'tgach avtomatik tizimga kiritish
            return redirect('parking_dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


# 2. Asosiy boshqaruv paneli (Faqat tizimga kirgan adminlar ko'ra oladi)
@login_required
def parking_dashboard(request):
    active_cars = CarParking.objects.filter(is_active=True)

    # 🔍 QIDIRUV TIZIMI LOGIKASI
    search_query = request.GET.get('q', '').strip()
    if search_query:
        # Raqami yoki rusumi bo'yicha qidirish (katta-kichik harfni farqlamaydi)
        active_cars = active_cars.filter(
            models.Q(plate_number__icontains=search_query) |
            models.Q(car_model__icontains=search_query)
        )

    receipt_id = request.GET.get('receipt_id')
    receipt = None
    if receipt_id:
        receipt = CarParking.objects.filter(id=receipt_id).first()

    current_count = CarParking.objects.filter(is_active=True).count()
    free_spaces = 200 - current_count

    return render(request, 'dashboard.html', {
        'cars': active_cars,
        'free_spaces': free_spaces,
        'current_count': current_count,
        'search_query': search_query,
        'receipt': receipt,
    })


# 3. Yangi mashina kiritish funksiyasi
@login_required
def park_car(request):
    if request.method == "POST":
        current_cars_count = CarParking.objects.filter(is_active=True).count()

        # 200 ta joy borligini tekshirish
        if current_cars_count >= 200:
            messages.error(request, "Stayankada joy qolmadi! Maksimal sig'im: 200")
            return redirect('parking_dashboard')

        plate_number = request.POST.get('plate_number').upper().strip()
        car_model = request.POST.get('car_model').strip()

        # Dublikat mashinalarni tekshirish
        already_parked = CarParking.objects.filter(plate_number=plate_number, is_active=True).exists()
        if already_parked:
            messages.error(request, f"Xatolik! {plate_number} raqamli avtomobil hozirda stayanka ichida turibdi.")
            return redirect('parking_dashboard')

        CarParking.objects.create(plate_number=plate_number, car_model=car_model)
        messages.success(request, f"{plate_number} raqamli mashina muvaffaqiyatli kiritildi.")
        return redirect('parking_dashboard')


# 4. Mashinani stayankadan chiqarish funksiyasi
@login_required
def unpark_car(request, car_id):
    car = CarParking.objects.get(id=car_id)
    car.calculate_fee()

    messages.success(request, f"{car.plate_number} chiqib ketdi. To'lov: {car.total_charge} so'm.")
    return redirect(f"{reverse('parking_dashboard')}?receipt_id={car.id}")


@login_required
def car_detail(request, car_id):
    car = get_object_or_404(CarParking, id=car_id)
    return render(request, 'car_detail.html', {'car': car})


@login_required
def get_cars(request):
    # Redirect to the main dashboard (avoids rendering a missing template)
    return redirect('parking_dashboard')