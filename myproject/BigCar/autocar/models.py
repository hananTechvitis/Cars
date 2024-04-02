from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='car_images')

    # New fields
    passengers = models.IntegerField(verbose_name='Number of Passengers')
    TYPE_CHOICES = (
        ('Hybrid', 'Hybrid'),
        ('Gasoline', 'Gasoline'),
    )
    type = models.CharField(max_length=8, choices=TYPE_CHOICES, default='Gasoline', verbose_name='Car Type')
    is_automatic = models.BooleanField(default=True, verbose_name='Is Automatic')
    fuel_efficiency = models.CharField(max_length=15, verbose_name='Fuel Efficiency (km/litre)')
    
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
