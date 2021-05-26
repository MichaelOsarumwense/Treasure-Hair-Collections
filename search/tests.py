from django.test import TestCase, Client


c = Client()


# Create your tests here.
class TestSearchViews(TestCase):

    def test_search_redirects_to_all_products_page(self):
        page = c.get("/search/?q=texas")
        self.assertEqual(page.status_code, 200)
