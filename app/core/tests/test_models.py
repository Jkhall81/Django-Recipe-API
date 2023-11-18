'''
Tests for models
'''
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    '''Testing models, as per the name'''

    def test_create_user_with_email(self):
        '''Test creating a user with an email'''
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email, 
            password=password,
            )
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        