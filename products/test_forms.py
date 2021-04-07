from django.test import TestCase
from .forms import ProductForm


class TestItemForm(TestCase):

    def test_products_form(self):
        form = ProductForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])
