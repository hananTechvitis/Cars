import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BigCar.settings")
django.setup()

from autocar.models import Brand

def import_brands_from_csv(csv_filename):
    with open(csv_filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        brands_added = 0
        for row in reader:
            _, created = Brand.objects.get_or_create(name=row['Brand'])
            if created:
                brands_added += 1
        print(f"Successfully added {brands_added} new brands.")

if __name__ == '__main__':
    import_brands_from_csv('brands.csv')
