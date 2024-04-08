from django.test import TestCase
from .models import MyModel

class MyModelTestCase(TestCase):
    def setUp(self):
        # Set up any necessary data or state before running each test method
        self.my_instance = MyModel.objects.create(name='Test Name', description='Test Description')

    def test_my_model_creation(self):
        # Test if the MyModel object was created successfully
        self.assertEqual(self.my_instance.name, 'Test Name')
        self.assertEqual(self.my_instance.description, 'Test Description')

