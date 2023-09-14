from django.test import TestCase 
from . import Menu


class MenuViewTest(TestCase):
    def setup(self):
      self.menu = Menu()
      self.id = Menu.objects.create(
         title = "TesteTitle",
         price = 333,
         inventory = 9
      ).id


    def test_getall():
      pass