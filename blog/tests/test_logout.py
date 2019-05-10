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
        self.post = Post.objects.create(title='test post', content='test post', author=self.user)

    def test_logout(self):
        self.client.login(**self.credentials)

        # signing out
        request = self.client.logout()

    def test_logout_get(self):
        self.client.post(reverse('logout'))
        response = self.client.get(reverse('post-update', kwargs={'pk': self.post.id}))
        self.assertRedirects(response, f'/login/?next=/post/{self.post.id}/update/')

