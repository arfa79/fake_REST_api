from django.test import TestCase
from django.urls import reverse

from fake_rest_app.models import Item

class ItemListViewTests(TestCase):
    def test_item_list_view_status_code(self):
        response = self.client.get(reverse('item-list'))
        self.assertEqual(response.status_code, 200)

    def test_item_list_view_no_items(self):
        response = self.client.get(reverse('item-list'))
        self.assertContains(response, "No items available.")

    def test_item_list_view_with_items(self):
        Item.objects.create(name='Item 1', description='Description 1', price=10.99)
        response = self.client.get(reverse('item-list'))
        self.assertQuerysetEqual(response.context['items'], ['<Item: Item 1>'])
