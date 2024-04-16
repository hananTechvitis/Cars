import csv
import os
import django
import requests  # Import requests to handle URL downloading
from django.core.files.base import ContentFile

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BigCar.settings")
django.setup()

from autocar.models import Car, Brand

def download_and_save_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        return ContentFile(response.content)
    else:
        return None

def import_cars_from_csv(csv_filename):
    with open(csv_filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        cars_added = 0
        for row in reader:
            brand_name = row['Brand']
            brand, _ = Brand.objects.get_or_create(name=brand_name)

            image_content = download_and_save_image(row['Image']) if 'Image' in row and row['Image'] else None

            car_defaults = {
                'year': int(row['Year']),
                'price': float(row['Price']),
                'passengers': int(row['Passengers']),
                'type': row['Type'],
                'is_automatic': row['Is Automatic'].lower() in ['true', '1', 't', 'yes'],
                'fuel_efficiency': row['Fuel Efficiency'],
                'image': image_content  # Handle image as a file
            }

            car, created = Car.objects.update_or_create(
                brand=brand,
                model=row['Model'],
                defaults=car_defaults
            )
            if created and image_content:
                car.image.save(f"{brand_name}_{row['Model']}.jpg", image_content, save=True)
                cars_added += 1
        print(f"Successfully added {cars_added} new cars.")

if __name__ == '__main__':
    import_cars_from_csv('cars.csv')
