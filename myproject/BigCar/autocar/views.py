from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST


def hello(request):
    return HttpResponse("Hello, world! This is my first Django view.")

def home(request):
    # Fetch the last 5 cars added to the database
    featured_cars = Car.objects.all().order_by('-id')[:5]
    # Pass the cars to the template
    return render(request, 'home.html', {'featured_cars': featured_cars})
   

@require_POST
def rent_car(request, car_id):
    if request.is_ajax():
        car = get_object_or_404(Car, id=car_id)
        # Add your rental logic here

        # Example: Add a success message
        message = "Car rental request submitted successfully for {}!".format(car.model)
        
        # Instead of adding a message to Django's messages framework, 
        # return a JSON response with the message
        return JsonResponse({'message': message}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)














def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars.html', {'cars': cars})



def image_view(request):
    return render(request, 'image.html')
