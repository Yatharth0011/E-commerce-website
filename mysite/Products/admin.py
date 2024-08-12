from django.contrib import admin
from .models import Products, ContactForm

class ProductsAdmin(admin.ModelAdmin):
    list_display=('name','price','quantity')

admin.site.register(Products, ProductsAdmin)
admin.site.register(ContactForm)