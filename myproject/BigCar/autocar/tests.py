from django.test import TestCase
from .models import Brand, Car
from django.core.files.uploadedfile import SimpleUploadedFile
import os

class CarModelTestCase(TestCase):
    def setUp(self):
        # Set up any necessary data or state before running each test method
        self.brand = Brand.objects.create(name='Toyota')

        # Creating a dummy image for testing
        image_path = os.path.join(os.path.dirname(__file__), 'media', 'car_images', 'R.png')
        self.image = SimpleUploadedFile(
            name='test_image.png',
            content=open(image_path, 'rb').read(),
            content_type='image/png'
        )

        self.car = Car.objects.create(
            brand=self.brand,
            model='Camry',
            year=2022,
            price=25000.00,
            image=self.image,  # Attach the image to the model
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
        self.assertTrue(self.car.image)  # Test if image is attached successfully

    def test_car_creation_and_list_view(self):
        # Test if the Car instance exists and its model attribute is correct
        self.assertEqual(self.car.model, 'Camry')
