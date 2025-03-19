from django.test import TestCase

from django.contrib.auth.models import User


class LoginTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_login(self):
        response = self.client.post('/user/login/', {'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/user/login/', {'username': 'testuser', 'password': 'wrongpass'})
        self.assertEqual(response.status_code, 401)

        response = self.client.post('/user/login/', {'username': 'wronguser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 401)

        response = self.client.post('/user/login/', {'username': 'wronguser', 'password': 'wrongpass'})
        self.assertEqual(response.status_code, 401)

        response = self.client.post('/user/login/', {'username': '', 'password': 'testpass'})
        self.assertEqual(response.status_code, 400)

        response = self.client.post('/user/login/', {'username': 'testuser', 'password': ''})
        self.assertEqual(response.status_code, 400)

        response = self.client.post('/user/login/', {'username': '', 'password': ''})
        self.assertEqual(response.status_code, 400)

        response = self.client.post('/user/login/', {'username': '', 'password': 'wrongpass'})
        self.assertEqual(response.status_code, 400)

        response = self.client.post('/user/login/', {'username': 'wronguser', 'password': ''})
        self.assertEqual(response.status_code, 400)

    # def test_sum(self):
    #     self.assertEqual(1 + 1, 2)
