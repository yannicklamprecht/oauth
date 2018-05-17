import urllib.request

from flask import Response

from oauth.src.server import callback
from oauth.tests.integration_test_base import IntegrationTestBase


class TestHello(IntegrationTestBase):
    def test_authenticate(self):
        response = urllib.request.urlopen("http://localhost:5000/authenticate")


    def test_callback(self):
        response = urllib.request.urlopen(
            'http://localhost:5000/callback?code=4/AACUz18wREwj3l1TFMT1XQEj8z_eUJBrJbm2e-X58tXOJKq_528pgUopfH8G56QOUIMnGDNLwB7Ono6h5E3-pl0#')
        result: Response = response
        self.assertEqual(200, result.status)
