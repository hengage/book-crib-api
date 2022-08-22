from django.test import TestCase
from unittest import mock

from django.contrib.auth import get_user_model

Author = get_user_model()

class TestAuthorModel(TestCase):
    
    def setUp(self):
        self.author = Author.objects.create(
            email='user@user.com',
            first_name='user1',
            last_name='user1',
            password='userpassword',
        )
        self.author2 = Author.objects.create(
            email='user2@user.com',
            first_name='user2',
            last_name='user2',
            password='userpassword',
        )

    def test_user_is_created_correctly(self):
        self.assertEquals(self.author.email, 'user@user.com')
        self.assertEquals(self.author.first_name, 'user1')
        self.assertEquals(self.author.last_name, 'user1')
        self.assertEquals(self.author.password, 'userpassword')
        self.assertEquals(self.author.id, 1)
