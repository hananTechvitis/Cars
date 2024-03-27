from django.shortcuts import render
from django.http import HttpResponse
from .models import Car

def hello(request):
    return HttpResponse("Hello, world! This is my first Django view.")

def home(request):
    return render(request, 'frontend/home.html')

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'frontend/cars.html', {'cars': cars})