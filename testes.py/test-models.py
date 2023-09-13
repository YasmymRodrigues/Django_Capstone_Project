from django.test import TestCase 
from . import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Pasta with Shrimp", price=30, inventory=4)
        self.assertEqual(item, "Pasta with Shrimp : 30")