from django.test import TestCase, Client
from ..views import PostCreateView
from django.contrib.auth.models import User
from ..models import Post
from django.urls import reverse

class PostDeleteViewTest(TestCase):

    def setUp(self):
        '''This is ran before each and every test!'''
        self.user = User.objects.create_user(username='test_user', password='password123')
        self.post = Post.objects.create(title='test post', content = 'test post', author=self.user)

    def test_assert_posts(self):
        self.assertEqual(Post.objects.count(), 1)

    def test_delete_redirect(self):
        '''assertRedirects tests where we are redirected after we delete
        this was defined in the settings.py file'''
        self.client.login(username='test_user', password='password123')
        response = self.client.post(reverse('post-delete', kwargs={'pk': self.post.id}))
        self.assertRedirects(response, '/')

    def test_delete_post(self):
        '''Assert that the object was actually deleted!'''
        self.client.login(username='test_user', password='password123')
        response = self.client.post(reverse('post-delete', kwargs={'pk': self.post.id}))
        self.assertEqual(Post.objects.count(), 0)



