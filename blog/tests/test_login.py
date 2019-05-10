from django.test import TestCase, Client
from django.contrib.auth.models import User
from ..models import Post
from django.urls import reverse


class PostDeleteViewTest(TestCase):

    def setUp(self):
        '''This is ran before each and every test!'''
        self.credentials = {
            'username': 'test_user',
            'password': 'password123'
        }
        self.user = User.objects.create_user(**self.credentials)

    def test_login(self):
        '''testing the login feature'''
        resp = self.client.login(**self.credentials)
        self.assertTrue(resp)

    def test_login_route(self):
        response = self.client.post(reverse('login'), data=self.credentials, follow=True)
        self.assertTrue(response)

    def test_logins(self):
        response = self.client.post('/login/', data=self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)


