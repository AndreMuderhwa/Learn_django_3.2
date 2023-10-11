from django.test import TestCase
import os
from django.conf import settings
from django.contrib.auth.password_validation import validate_password

class LeanDjangoTestConfig(TestCase):
   def test_secret_key_strength(self):
      SECRET_KEY=os.environ.get("DJANGO_SECRET_KEY")
      #self.assertNotEqual(SECRET_KEY,"abc1234")
      is_strong=validate_password(SECRET_KEY)
      