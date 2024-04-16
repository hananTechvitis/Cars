import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BigCar.settings")
django.setup()

from autocar.models import Car, Brand

def import_cars_from_csv(csv_filename):
    with open(csv_filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            brand, _ = Brand.objects.get_or_create(name=row['Brand'])
            car, created = Car.objects.update_or_create(
                brand=brand,
                model=row['Model'],
                defaults={
                    'year': int(row['Year']),
                    'price': float(row['Price']),
                    'passengers': int(row['Passengers']),
                    'type': row['Type'],
                    'is_automatic': row['Is Automatic'].lower() in ['true', '1', 't', 'yes'],
                    'fuel_efficiency': row['Fuel Efficiency'],
                    'image_url': row['Image']
                }
            )
