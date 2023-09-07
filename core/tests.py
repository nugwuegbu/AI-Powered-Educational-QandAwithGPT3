import os,django
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from account.models import User


# Create your tests here.
SEARCH_TEXT_URL = reverse('search')

class TestSearchAPIView(APITestCase):
    def setUp(self):
        # self.client = APIClient()

        self.user = User(username='admin1',first_name='godfrey',last_name='abas',email='admin1@gmail.com')
        self.user.is_superuser = True
        self.user.set_password('welcome')
        self.user.save()
        # self.client.login(username='admin1',password='admin1')
    def test_search_text(self):
        self.assertTrue(self.client.login(username='admin1',password='welcome'))
        payload = {
            "search_text":"what is love?"
        }
        response = self.client.post(SEARCH_TEXT_URL,payload,format='json')
        self.assertEquals(response.status_code,status.HTTP_200_OK)
