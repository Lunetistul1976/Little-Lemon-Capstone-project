from django.test import TestCase
from django.urls import reverse
from restaurant.models import Menu
from restaurant.views import MenuItemView
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.menu_test1 = Menu.objects.create(
            Title='Pizza',
            Price=20,
            Inventory=40,
        )

        self.menu_test2 = Menu.objects.create(
            Title='Icecream',
            Price=10,
            Inventory=50,
        )

        self.menu_test3 = Menu.objects.create(
            Title='Bruschetta',
            Price=5,
            Inventory=10,
        )

    def test_menu_list_view(self):
        url = reverse('restaurant/menu')  # Use the name of your URL pattern
        request = self.client.get(url)

        response = MenuItemView(request)

        self.assertEqual(response.status_code, 200)

        # Serialize the data from the database
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        
        # Compare serialized data to the content of the response
        self.assertJSONEqual(str(response.content, encoding='utf8'), serializer.data)
