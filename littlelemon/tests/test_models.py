from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
 def instance(self):
  menu_test = Menu.objects.create(
   Title = 'Beef Stake',
   Price = 12,
   Inventory = 3,

  )
  self.assertEqual(menu_test,'Beef Stake : 12' )