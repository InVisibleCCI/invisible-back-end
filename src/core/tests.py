from django.urls import reverse
from rest_framework.test import APITestCase

from core.models import User


class UserAPIViewTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            "toto@toto.com",
            "toto"
        )
        self.user.save()

    def test_connection_with_good_credentials(self):
        payload = {
            "email" : "toto@toto.com",
            "password" : "toto"
        }
        response = self.client.post(reverse("token_obtain_pair"), payload)
        self.assertEqual(200, response.status_code)

    def test_connection_with_bad_credentials(self):
        payload = {
            "email" : "t@toto.com",
            "password" : "toto"
        }
        response = self.client.post(reverse("token_obtain_pair"), payload)
        self.assertEqual(401, response.status_code)

