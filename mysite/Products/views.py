from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

def home(request):
    products = Products.objects.all()  # Fetch all products from the database
    return render(request, 'home.html', {'products': products})