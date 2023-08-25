from django.test import TestCase
from django.urls import reverse

from .models import Item
class ItemApiTests(TestCase):
    def setUp(self):
        Item.objects.create(name='Test Item', description='Test Description')

    def test_item_list(self):
        response = self.client.get(reverse('item-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Item')

