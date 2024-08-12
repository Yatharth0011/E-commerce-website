from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
from .models import ContactForm

def home(request):
    products = Products.objects.all()  # Fetch all products from the database
    return render(request, 'home.html', {'products': products})
def ContactFormView(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        phonenum=request.POST['phonenum']
        message=request.POST['message']
        contact=ContactForm(name=name,email=email,phonenum=phonenum,message=message)
        contact.save()
    return render(request, 'home.html')