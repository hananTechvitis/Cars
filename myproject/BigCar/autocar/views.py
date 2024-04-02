from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect

def hello(request):
    return HttpResponse("Hello, world! This is my first Django view.")

def home(request):
    # Fetch the last 5 cars added to the database
    featured_cars = Car.objects.all().order_by('-id')[:5]
    # Pass the cars to the template
    return render(request, 'home.html', {'featured_cars': featured_cars})
   

def rent_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    # Example action: print a message to the console (replace with your action)
    print(f"The car {car} has been requested for rent.")
    # Add your logic here (e.g., create a rental record, mark the car as unavailable)
    
    # Optionally, add a message to display to the user
    messages.success(request, "Your rental request has been submitted.") 
    messages.success(request, "Your rental request for the car has been submitted successfully!")
    
    # Redirect to a new URL:
    return redirect('home')  # Redirect to the homepage or another appropriate page














def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars.html', {'cars': cars})



def image_view(request):
    return render(request, 'image.html')
