from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class StaticViewTest(TestCase):

    def setUp(self):
        '''This is ran before each and every test!'''
        self.user = User.objects.create_user(username='test_user', password='password123')
        self.post = Post.objects.create(title='test post', content = 'test post', author=self.user)
        self.url = 'https://django-blog-aws-deployment.s3.amazonaws.com/default.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIATU2WVWJSEDA64YED%2F20190401%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20190401T165351Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=610328cbdf03bd5c7dfe83d6043913e517cd20211254db77de5d43c6de2bf9bb'

    # def test_static_files(self):
    #     '''Checks whether the response contains the main.css file'''
    #     response = self.client.get(reverse('/profile/'))
    #     self.assertContains(response, self.url)




