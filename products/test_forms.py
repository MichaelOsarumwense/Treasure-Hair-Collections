from django.test import TestCase
from .forms import Product


class TestItemForm(TestCase):

    def test_products_form(self):
        form = Product('categories', {})
        self.assertFalse(form.image)
