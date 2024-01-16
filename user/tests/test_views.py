from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from user.models import Profile
from user.forms import ProfileForm


class ProfileViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.profile = Profile.objects.create(
            user=self.user,
            first_name='Test',
            last_name='User',
            address1='123 High Street',
            post_code='12345',
            city='Cardiff',
            country='UK',
            email='test@example.com',
            telephone='1234567890',
        )

    def test_profile_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('user:profile_detail', kwargs={'pk': self.user.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/profile_detail.html')
        self.assertEqual(response.context['profile'], self.profile)


class ProfileCreateViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_profile_create_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('user:profile_create', kwargs={'pk': self.user.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/profile_form.html')

        form_data = {
            'first_name': 'Test',
            'last_name': 'User',
            'address1': '123 High Street',
            'post_code': '12345',
            'city': 'Cardiff',
            'country': 'UK',
            'email': 'test@example.com',
            'telephone': '1234567890',
        }

        response = self.client.post(reverse('user:profile_create', kwargs={'pk': self.user.id}), data=form_data)
        self.assertEqual(response.status_code, 200)  
        

class ProfileUpdateViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.profile = Profile.objects.create(
            user=self.user,
            first_name='Test',
            last_name='User',
            address1='123 High Street',
            post_code='12345',
            city='Cardiff',
            country='UK',
            email='test@example.com',
            telephone='1234567890',
        )

    def test_profile_update_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('user:profile_update', kwargs={'pk': self.user.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/profile_form.html')

        form_data = {
            'first_name': 'Updated Test',
            'last_name': 'Updated User',
            'address1': 'Updated 123 High Street',
            'post_code': '54321',
            'city': 'Updated Cardiff',
            'country': 'US',
            'email': 'updated_test@example.com',
            'telephone': '9876543210',
        }

        response = self.client.post(reverse('user:profile_update', kwargs={'pk': self.user.id}), data=form_data)
        self.assertEqual(response.status_code, 302)  # Redirect on successful form submission
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.first_name, 'Updated Test')


class ProfileDeleteViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.profile = Profile.objects.create(
            user=self.user,
            first_name='Test',
            last_name='User',
            address1='123 High Street',
            post_code='12345',
            city='Cardiff',
            country='UK',
            email='test@example.com',
            telephone='1234567890',
        )

    def test_profile_delete_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('user:profile_delete', kwargs={'pk': self.user.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/profile_delete.html')

        response = self.client.post(reverse('user:profile_delete', kwargs={'pk': self.user.id}))
        self.assertEqual(response.status_code, 302)  # Redirect on successful deletion
        self.assertFalse(Profile.objects.filter(user=self.user).exists())
