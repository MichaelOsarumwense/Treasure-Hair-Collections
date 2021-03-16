from django.test import TestCase
from .models import Product, Category


class Test1(TestCase):

    def test_model_name(self):
        product = Product(name="Test product",
                          description="Test description",
                          price=2.10)
        self.assertTrue(product.name)

    def test_model_image(self):
        product = Product(name="Test product",
                          description="Test description",
                          price=2.10)
        self.assertFalse(product.image)

    def test_category(self):
        category = Category('name', '')
        self.assertFalse(category.name)
