# profiles/tests/test_models.py
from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from user.models import Profile
from django.core.exceptions import ValidationError

class ProfileModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.profile = Profile.objects.create(
            first_name='John',
            last_name='Smith',
            address1='123 Main Street',
            post_code='12345',
            city='London',
            country='UK',
            email='john@example.com',
            telephone='1234567890',
            user=self.user,
        )


    def test_profile_creation(self):
        self.assertTrue(isinstance(self.profile, Profile))
        self.assertEqual(Profile.objects.count(), 1)


    def test_str_method(self):
        self.assertEqual(str(self.profile), 'testuser')
        
        
    def test_user_profile_connection(self):
        # Retrieve the user's profile and check if it matches the created profile
        user_profile = Profile.objects.get(user=self.user)
        self.assertEqual(user_profile, self.profile)

