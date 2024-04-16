from django.test import TestCase
from .models import Brand, Car

class CarModelTest(TestCase):
    def setUp(self):
        # Setting up test data
        self.brand = Brand.objects.create(name="Test Brand")
        self.car = Car.objects.create(
            brand=self.brand,
            model="Model X",
            year=202a,
            price=50000.00,z
            type='Gasoline',
            is_automatic=True,
            fuel_efficiency='15 km/litre'
        )

    def test_string_representation(self):
        self.assertEqual(str(self.car), "Test Brand Model X (2020)")

    def test_brand_cascade_delete(self):
        # Test cascading delete
        self.brand.delete()
        self.assertEqual(Car.objects.count(), 0)

    def test_field_defaults(self):
        # Test defaults
        new_car = Car.objects.create(brand=self.brand, model="Model Y", year=2021, price=60000.00)
        self.assertEqual(new_car.passengers, 4)
        self.assertTrue(new_car.is_automatic)
