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
    image = models.ImageField(upload_to='car_images/', blank=True, null=True)  # Added ImageField here

    # New fields
    passengers = models.IntegerField(verbose_name='Number of Passengers', default=4)
    TYPE_CHOICES = (
        ('Hybrid', 'Hybrid'),
        ('Gasoline', 'Gasoline'),
    )
    type = models.CharField(max_length=8, choices=TYPE_CHOICES, default='Gasoline', verbose_name='Car Type')
    is_automatic = models.BooleanField(default=True, verbose_name='Is Automatic')
    fuel_efficiency = models.CharField(max_length=15, verbose_name='Fuel Efficiency (km/litre)', default='N/A')
    
    def image_url(self):
        """
        Returns the URL of the image, checking both .jpeg and .jpg extensions.
        """
        base_path = os.path.join('car_images', f'{self.model}')
        jpeg_path = f'{base_path}.jpeg'
        jpg_path = f'{base_path}.jpg'

        if os.path.exists(os.path.join(settings.MEDIA_ROOT, jpeg_path)):
            return os.path.join(settings.MEDIA_URL, jpeg_path)
        elif os.path.exists(os.path.join(settings.MEDIA_ROOT, jpg_path)):
            return os.path.join(settings.MEDIA_URL, jpg_path)
        return None  # or a default image path

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
