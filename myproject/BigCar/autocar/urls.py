from django.urls import path
from . import views



urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('', views.home, name='home'),
    path('cars/', views.car_list, name='cars'),
    path('image/', views.image_view, name='image-view'),
]
