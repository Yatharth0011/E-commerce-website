from django.db import models

class Products(models.Model):
    name=models.CharField(max_length=255)
    price=models.FloatField()
    quantity=models.IntegerField()
    image = models.ImageField(upload_to='', blank=True, null=True)
    
class ContactForm(models.Model):
    name=models.CharField(max_length=255)
    phonenum=models.CharField(max_length=13)
    email=models.CharField(max_length=100)
    message=models.TextField(max_length=2000)

    def __str__(self):
        return self.name
