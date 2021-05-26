from django.test import TestCase
from .forms import UserProfileForm

# Create your tests here.


class TestProfileForms(TestCase):

    def test_create_profile_form_with_required_fields_filled(self):
        form = UserProfileForm({
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
            'default_country': "US",
        })
        self.assertTrue(form.is_valid())
