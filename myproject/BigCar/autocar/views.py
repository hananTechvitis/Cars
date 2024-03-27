from django.shortcuts import render
from .models import Car
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, world! This is my first Django view.")