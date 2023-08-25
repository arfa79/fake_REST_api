from django.test import TestCase
from fake_rest_app.models import Item

class ItemModelTests(TestCase):
    def test_item_str_representation(self):
        item = Item(name='Test Item', description='Test Description', price=10.99)
        self.assertEqual(str(item), 'Test Item')
