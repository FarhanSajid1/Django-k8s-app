from django.test import TestCase

class ProfileTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        print('setupTestdata: Run once to set up non-modified data for all class methods')


    def setUp(self):
        '''Ran once for every test method'''
        pass

    