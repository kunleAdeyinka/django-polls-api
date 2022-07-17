from urllib import request
from rest_framework.test import APITestCase
from rest_framework.test import APIClient

from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from polls import apiviews


class TestPoll(APITestCase):
    def setUp(self):
        self.factory = APIClient()
        self.view = apiviews.PollViewSet.as_view({'get': 'list'})
        self.uri = '/polls/'
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            'test',
            email='testuser@test.com',
            password='test'
        )

    # A test to view the polls list.
    def test_list(self):
        self.client.login(username="test", password="test")
        response = self.client.get(self.uri)
        self.assertEqual(
            response.status_code, 
            200,
            'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code)
        )

    def test_create(self):
        self.client.login(username="test", password="test")
        params = {
            "question": "How are you",
            "created_by": 1
        }
        response = self.client.post(self.uri, params)
        self.assertEquals(
            response.status_code, 
            201,
            'Expected Response Code 201, received {0} instead.'
                         .format(response.status_code)
        )

