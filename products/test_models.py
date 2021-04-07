from django.test import TestCase
from .models import Product, Category


class Test1(TestCase):

    def test_model_name(self):
        product = Product(name="Test product",
                          description="Test description",
                          price=2.10)
        self.assertEquals(product.name, "Test product")

    def test_model_image(self):
        product = Product(image="https://imgur.com/fZFqpPg.jpg")
        self.assertEquals(product.image, "https://imgur.com/fZFqpPg.jpg")

    def test_category(self):
        category = Category('name', 'wigs')
        self.assertEquals(category.name, "wigs")
