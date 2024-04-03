from django.urls import path
from . import views



urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('', views.home, name='home'),
    path('cars/', views.car_list, name='cars'),
    path('image/', views.image_view, name='image-view'),
    path('rent-car/<int:car_id>/', views.rent_car, name='rent-car'),
    path('payment/<int:car_id>/', views.payment, name='payment'),
]
