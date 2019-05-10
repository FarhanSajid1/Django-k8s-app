from django.test import TestCase, Client
from ..views import PostCreateView
from django.contrib.auth.models import User
from ..models import Post
from django.urls import reverse

class UpdateViewTest(TestCase):

    def setUp(self):
        '''This is ran before each and every test!'''
        self.user = User.objects.create_user(username='test_user', password='password123')
        self.post = Post.objects.create(title='test post', content = 'test post', author=self.user)

    def test_redirecting_post(self):
        '''Test whether we get redirected if we are not logged in!
        pk is necesary because the post-update view requires pk as the post id'''
        response = self.client.get(reverse('post-update', kwargs={'pk':self.post.id}))
        self.assertRedirects(response, f'/login/?next=/post/{self.post.id}/update/')

    def test_forwarding_with_proper_user(self):
        '''Test whether we get redirected if we are not logged in!
        pk is necesary because the post-update view requires pk as the post id'''
        '''there is no redirect, this is a forward... we have the proper authority to update'''
        self.client.login(username='test_user', password='password123')
        response = self.client.post(reverse('post-update', kwargs={'pk':self.post.id}))
        self.assertEqual(response.status_code, 200)

    def test_modifying_post(self):
        '''Test updating the post
        pk is necessary for the post unique identifier'''
        self.client.force_login(User.objects.get_or_create(username='test_user')[0]) # we login so we can modify our own post
        self.client.post(reverse('post-update', kwargs={'pk': self.post.id}),{'title': 'testing new post', 'content': 'hello there','author': self.user})
        self.assertEqual(Post.objects.first().title, 'testing new post')

    def test_modifying_post_unauthorized(self):
        '''Ensure that unauthorized users cannot modify other poeple's content'''
        self.client.force_login(User.objects.get_or_create(username='unauthorized')[0])
        self.response = self.client.post(reverse('post-update', kwargs={'pk': self.post.id}))
        self.assertEqual(self.response.status_code, 403)
        print(Post.objects.count()) # there is only 1 post ever during all of these tests
