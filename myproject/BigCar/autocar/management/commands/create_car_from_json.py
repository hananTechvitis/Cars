from django.core.management.base import BaseCommand
import json
from autocar.models import Brand, Car

class Command(BaseCommand):
    help = 'Create a car from JSON data'

    def handle(self, *args, **options):
        # JSON data as a string
        json_data = '''
        {
            "brand": "Toyota",
            "model": "Corolla",
            "year": 2022,
            "price": 344,
            "image": "car_images/coro.jpeg",
            "passengers": 4,
            "type": "Gasoline",
            "is_automatic": true,
            "fuel_efficiency": "45 km/litre"
        }
        '''

        # Convert JSON string to Python dictionary
        car_info = json.loads(json_data)

        # Ensure the brand exists or create it
        brand, created = Brand.objects.get_or_create(name=car_info['brand'])

        # Create the car
        car = Car.objects.create(
            brand=brand,
            model=car_info['model'],
            year=car_info['year'],
            price=car_info['price'],
            image=car_info['image'],
            passengers=car_info['passengers'],
            type=car_info['type'],
            is_automatic=car_info['is_automatic'],
            fuel_efficiency=car_info['fuel_efficiency']
        )

        self.stdout.write(self.style.SUCCESS(f"Car created: {car}"))

