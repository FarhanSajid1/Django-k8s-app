from django.test import TestCase, Client
from ..views import PostCreateView
from django.contrib.auth.models import User
from ..models import Post
from django.urls import reverse



class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        '''Creating a user and a post
        this is only ran once for the entire test!
        setUP is an instance method and is run on every test'''
        cls.user = User.objects.create_user(username='farhans', password='passsword123')
        cls.user.save()
        # Post.objects.create(title="my first post", content= "farhan's first post", author = cls.user)
    #
    def test_published_post(self):
        self.client.force_login(User.objects.get_or_create(username='farhans')[0])
        self.client.post(reverse('post-create'), {'title': 'testing post', 'content': 'testing content', 'author': self.user})
        self.assertEqual(Post.objects.first().title, 'testing post')
    #
    def test_post_count(self):
        self.user = self.client.force_login(User.objects.get_or_create(username='farhans')[0])
        self.client.post(reverse('post-create'), {'title': 'testing post', 'content': 'testing content', 'author': self.user})
        self.assertEqual(Post.objects.count(), 1) # we create a post at start up


    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('post-create'))
        self.assertRedirects(response, '/login/?next=/post/new/')

