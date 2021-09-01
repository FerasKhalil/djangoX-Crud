from django.test import TestCase 
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Snack

# Create your tests here.

class SnacksTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'Firas', email = 'x.firashasan@gmail.com', password = '2171987'
        )
        self.snack = Snack.objects.create(
            title = 'Zinger', description  = 'Delicious', purchaser = self.user
        )
    def test_StringRepresentation(self):
        self.assertEqual(str(self.snack), "Zinger")

    def test_SnackContent(self):
        self.assertEqual(f"{self.snack.title}", 'Zinger')
        self.assertEqual(f"{self.snack.description}", 'Delicious')
        self.assertEqual(self.snack.purchaser, self.user)

    def test_SnackListView(self):
        url = reverse('snack_list')
        actual = self.client.get(url).status_code
        self.assertEqual(actual, 200)

    def test_SnackUpdateView(self):
        response = self.client.post(reverse('snack_update', args='1'), {'title':'Pepsi'})
        self.assertContains(response, 'Pepsi')
        
    def test_SnackDeleteView(self):
        response = self.client.get(reverse("snack_delete", args="1"))
        self.assertEqual(response.status_code, 200)