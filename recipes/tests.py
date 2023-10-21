from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.

User=get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        self.user_a=User.objects.create_user('andrew',password='123')
    
    def test_user_pwd(self):
        checked=self.user_a.check_password('123')
        self.assertTrue(checked)