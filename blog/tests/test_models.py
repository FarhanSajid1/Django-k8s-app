from django.test import TestCase
from ..models import Post
from django.contrib.auth.models import User

class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        '''Creating a user and a post'''
        user = User.objects.create_user(username='farhans', password='passsword123')
        Post.objects.create(title="my first post", content= "farhan's first post", author = user)


    def test_title_field(self):
        self.assertEqual(Post.objects.get().title,"my first post")

    def test_post_content(self):
        self.assertEqual(Post.objects.get().content, "farhan's first post")

    def test_item_was_created(self):
        '''ensure that an item was created'''
        self.assertEqual(Post.objects.count(), 1)

    def test_get_absolute_url(self):
        '''This tests the post url
        /post/<int:pk>/'''
        author = Post.objects.get(id=1)
        self.assertEquals(author.get_absolute_url(), '/post/1/')



