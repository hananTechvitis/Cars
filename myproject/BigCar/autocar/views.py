from django.shortcuts import render
from django.http import HttpResponse
from .models import Car

def hello(request):
    return HttpResponse("Hello, world! This is my first Django view.")

def home(request):
    return render(request, 'home.html')

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars.html', {'cars': cars})



def image_view(request):
    return render(request, 'image.html')
