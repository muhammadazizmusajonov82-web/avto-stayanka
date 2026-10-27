from datetime import timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import CarParking


class CheckoutReceiptTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='admin',
            password='securepass123'
        )
        self.car = CarParking.objects.create(
            plate_number='01A123AA',
            car_model='Nexia 3',
            arrival_time=timezone.now() - timedelta(hours=2, minutes=15),
            is_active=True,
        )

    def test_unpark_shows_receipt_on_dashboard(self):
        self.client.login(username='admin', password='securepass123')

        response = self.client.post(reverse('unpark_car', args=[self.car.id]))

        self.assertEqual(response.status_code, 302)
        dashboard_response = self.client.get(f"{reverse('parking_dashboard')}?receipt_id={self.car.id}")
        self.assertContains(dashboard_response, 'CHEK')
        self.assertContains(dashboard_response, '01A123AA')
        self.assertContains(dashboard_response, 'Nexia 3')
        self.assertContains(dashboard_response, 'so\'m')
