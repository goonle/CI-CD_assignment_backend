# from django.test import TestCase
#
# from django.contrib.auth.models import User
#
#
# class LoginTest(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', password='testpass')
#
#     def test_login(self):
#         response = self.client.post('/user/login/', {'username': 'testuser', 'password': 'testpass'})
#         self.assertEqual(response.status_code, 200)
#
#         response = self.client.post('/user/login/', {'username': 'testuser', 'password': 'wrongpass'})
#         self.assertEqual(response.status_code, 401)
#
#         response = self.client.post('/user/login/', {'username': 'wronguser', 'password': 'testpass'})
#         self.assertEqual(response.status_code, 401)
#
#         response = self.client.post('/user/login/', {'username': 'wronguser', 'password': 'wrongpass'})
#         self.assertEqual(response.status_code, 401)
#
#         response = self.client.post('/user/login/', {'username': '', 'password': 'testpass'})
#         self.assertEqual(response.status_code, 400)
#
#         response = self.client.post('/user/login/', {'username': 'testuser', 'password': ''})
#         self.assertEqual(response.status_code, 400)
#
#         response = self.client.post('/user/login/', {'username': '', 'password': ''})
#         self.assertEqual(response.status_code, 400)
#
#         response = self.client.post('/user/login/', {'username': '', 'password': 'wrongpass'})
#         self.assertEqual(response.status_code, 400)
#
#         response = self.client.post('/user/login/', {'username': 'wronguser', 'password': ''})
#         self.assertEqual(response.status_code, 400)
#
#     # def test_sum(self):
#     #     self.assertEqual(1 + 1, 2)

# test_auth.py
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserLoginTestCase(APITestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'
        }
        self.user = User.objects.create_user(**self.credentials)
        self.token_url = reverse('login')

    def test_token_login(self):
        # Simulate login to get token
        response = self.client.post(self.token_url, self.credentials)

        # Check if the response status is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the token is in the response
        self.assertIn('token', response.data)

        # Use the token to authenticate further requests
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)