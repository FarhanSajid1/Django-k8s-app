from django.test import TestCase, Client
from ..views import PostCreateView
from django.contrib.auth.models import User
from ..models import Post
import random
from django.urls import reverse

class DetailViewTest(TestCase):

    def setUp(self):
        '''This is ran before each and every test!'''
        self.user = User.objects.create_user(username='test_user', password='password123')
        self.post = Post.objects.create(title='test post', content = 'test post', author=self.user)
        self.post1 = Post.objects.create(title='test post', content='test post1', author=self.user)
        self.post2 = Post.objects.create(title='test post', content='test post2', author=self.user)
        self.post3 = Post.objects.create(title='test post', content='test post3', author=self.user)
        self.post4 = Post.objects.create(title='test post', content='test post4', author=self.user)
        self.post5 = Post.objects.create(title='test post', content='test post5', author=self.user)
        self.posts = [self.post, self.post1, self.post2, self.post3]

    def test_view(self):
        '''Making sure that we can view the post'''
        request =  self.client.get(reverse('post-detail', kwargs={"pk": self.post.id}))
        self.assertEqual(request.status_code, 200)

    def test_response(self):
        '''Ensuring that the request object renders the post properly'''
        request = self.client.get(reverse('post-detail', kwargs={"pk": self.post.id}))
        self.assertContains(request, 'test post')

