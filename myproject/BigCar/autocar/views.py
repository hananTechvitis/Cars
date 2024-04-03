from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
from django.shortcuts import redirect
from django.contrib import messages


def hello(request):
    return HttpResponse("Hello, world! This is my first Django view.")

def home(request):
    # Fetch the last 5 cars added to the database
    featured_cars = Car.objects.all().order_by('-id')[:5]
    # Pass the cars to the template
    return render(request, 'home.html', {'featured_cars': featured_cars})
   


def rent_car(request, car_id):
    messages.success(request, "Car rented successfully!")

    # Redirect back to the same page or to a different page
    return redirect('home')


def payment(request, car_id):    
    context = {
        'car_id': car_id,
    }
    return render(request, 'myapp/payment.html', context)










def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars.html', {'cars': cars})



def image_view(request):
    return render(request, 'image.html')
