from django.test import TestCase


class CheckoutViews(TestCase):

    def test_checkout(self):
        response = self.client.get('/checkout')
        self.assertNotEqual(response.status_code, 404)

    def test_checkout_sucess(self):
        response = self.client.get('/checkout_success')
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "includes/mobile-top-header.html")
        self.assertTemplateUsed(response, "includes/main-nav.html")
