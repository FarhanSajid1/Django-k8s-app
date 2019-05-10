from django.test import TestCase, Client
from ..views import PostCreateView
from django.contrib.auth.models import User
from ..models import Post
import random
from django.urls import reverse

class UserPostViewTest(TestCase):

    def setUp(self):
        '''This is ran before each and every test!
        We want to ensure that all these posts are being rendered'''
        self.user = User.objects.create_user(username='test_user', password='password123')
        self.post = Post.objects.create(title='test post', content = 'test post', author=self.user)
        self.post1 = Post.objects.create(title='test post', content='test post1', author=self.user)
        self.post2 = Post.objects.create(title='test post', content='test post2', author=self.user)
        self.post3 = Post.objects.create(title='test post', content='test post3', author=self.user)
        self.post4 = Post.objects.create(title='test post', content='test post4', author=self.user)
        self.post5 = Post.objects.create(title='test post', content='test post5', author=self.user)

    # def test_user_posts_showing(self):
    #     request = self.client.get(reverse('user-posts', kwargs={'username': self.user.username}))
    #     self.assert

    def test_view_url_exists(self):
        '''Make sure that all the posts that we want actually exist
        this is done by checking the http status code:
        HTTP 2xx = sucessful
        HTTP 200 = OK
        HTTP 201 = Created
        http 204 = No Content

        HTTP 3xx = redirected
        301 = moved permanently
        302 = found by redirected'''
        request = self.client.get(reverse('user-posts', kwargs={'username': self.user.username}))
        self.assertEqual(request.status_code, 200)

    def test_render_template(self):
        '''Making sure that the proper template is rendered'''
        request = self.client.get(reverse('user-posts', kwargs={'username': self.user.username}))
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, 'blog/user_posts.html')


    def test_pagination_number(self):
        '''Making sure that the proper template is paginated'''
        request = self.client.get(reverse('user-posts', kwargs={'username': self.user.username}))
        self.assertEqual(request.status_code, 200)
        self.assertTrue('is_paginated' in request.context)
        self.assertTrue(request.context['is_paginated'] == True)

    def test_page_loading(self):
        '''Making sure that the proper template is rendered'''
        request = self.client.get(reverse('user-posts', kwargs={'username': self.user.username}))
        self.assertEqual(request.status_code, 200)

