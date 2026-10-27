from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from cars import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Bizning manzillarimiz:
    path('register/', views.register_admin, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', views.parking_dashboard, name='parking_dashboard'),
    path('park/', views.park_car, name='park_car'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('unpark/<int:car_id>/', views.unpark_car, name='unpark_car'),
    path('parking/', views.get_cars, name='get_cars'),
]
