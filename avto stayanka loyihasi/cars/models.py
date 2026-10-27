from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import math
from decimal import Decimal


class CarParking(models.Model):
    # Mashina ma'lumotlari
    plate_number = models.CharField(max_length=20, verbose_name="Mashina raqami")
    car_model = models.CharField(max_length=50, verbose_name="Mashina rusumi")

    # Vaqt ko'rsatkichlari
    arrival_time = models.DateTimeField(default=timezone.now, verbose_name="Kirgan vaqti")
    departure_time = models.DateTimeField(null=True, blank=True, verbose_name="Chiqqan vaqti")

    # Holat va To'lov
    is_active = models.BooleanField(default=True, verbose_name="Hozir stayankadami?")
    total_charge = models.DecimalField(max_digits=10, decimal_places=2, default=5000, verbose_name="To'lov summasi")

    def calculate_fee(self):
        """ Mashina chiqib ketayotganda to'lovni hisoblash funksiyasi """
        if not self.departure_time:
            self.departure_time = timezone.now()

        # Umumiy turgan vaqtni soniyalarda aniqlash
        duration = self.departure_time - self.arrival_time
        total_minutes = duration.total_seconds() / 60

        # Base fee: 5000 so'm that covers up to 1 hour 10 minutes (70 minutes).
        base_fee = Decimal('5000')
        extra_per_hour = Decimal('1500')

        if total_minutes <= 70:
            self.total_charge = base_fee
        else:
            # minutes after the free/base window
            extra_minutes = total_minutes - 70
            extra_hours = math.ceil(extra_minutes / 60)
            self.total_charge = base_fee + (extra_per_hour * Decimal(extra_hours))

        self.is_active = False
        self.save()

    @property
    def current_charge(self):
        """ Returns the current charge (Decimal) for this parking record.
            If the car is still parked, computes based on now; otherwise returns stored total_charge.
        """
        base_fee = Decimal('5000')
        extra_per_hour = Decimal('1500')

        end_time = timezone.now() if self.is_active and not self.departure_time else (self.departure_time or timezone.now())
        duration = end_time - self.arrival_time
        total_minutes = duration.total_seconds() / 60

        if total_minutes <= 70:
            return base_fee
        extra_minutes = total_minutes - 70
        extra_hours = math.ceil(extra_minutes / 60)
        return base_fee + (extra_per_hour * Decimal(extra_hours))

    def __str__(self):
        return f"{self.plate_number} ({self.car_model})"

    # files: cars/models.py ichiga qo'shing

    def get_duration_string(self):
        """ Mashina hozirgacha necha soat va daqiqa turganini matn ko'rinishida qaytaradi """
        from django.utils import timezone

        # Agar mashina hali chiqib ketmagan bo'lsa, hozirgi vaqt bilan hisoblaydi
        end_time = self.departure_time if self.departure_time else timezone.now()
        duration = end_time - self.arrival_time

        total_seconds = int(duration.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60

        if hours > 0:
            return f"{hours} soat, {minutes} daqiqa"
        return f"{minutes} daqiqa"
