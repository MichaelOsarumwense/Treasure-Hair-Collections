from django.test import TestCase


class TestViews(TestCase):

    def test_all_products(self):
        response = self.client.get('/products')
        self.assertNotEqual(response.status_code, 500)
        self.assertTemplateNotUsed(response, 'products/edit_product.html')

    def test_get_product_detail(self):
        response = self.client.get('/product_detail')
        self.assertNotEqual(response.status_code, 500)
        self.assertTemplateNotUsed(response, 'products/add_product.html')
