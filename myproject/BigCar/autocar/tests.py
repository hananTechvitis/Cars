from django.test import TestCase
from .models import Brand, Car

class CarModelTestCase(TestCase):
    def setUp(self):
        # Set up any necessary data or state before running each test method
        self.brand = Brand.objects.create(name='Toyota')
        self.car = Car.objects.create(
            brand=self.brand,
            model='Camry',
            year=2022,
            price=25000.00,
            passengers=5,
            type='Gasoline',
            is_automatic=True,
            fuel_efficiency='12'
        )

    def test_car_model_creation(self):
        # Test if the Car object was created successfully
        self.assertEqual(self.car.model, 'Camry')
        self.assertEqual(self.car.year, 2022)
        self.assertEqual(self.car.price, 25000.00)
        self.assertEqual(self.car.passengers, 5)
        self.assertEqual(self.car.type, 'Gasoline')
        self.assertTrue(self.car.is_automatic)
        self.assertEqual(self.car.fuel_efficiency, '12')
