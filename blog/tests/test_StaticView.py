from django.test import TestCase, Client
from django.contrib.staticfiles import finders
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse

class StaticViewTest(TestCase):

    def test_static_files(self):
        '''Checks whether the response contains the main.css file'''
        response = self.client.get(reverse('blog-home'))
        self.assertContains(response, 'main.css')
