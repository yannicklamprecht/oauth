import urllib.request

from oauth.src.server import callback
from oauth.tests.integration_test_base import IntegrationTestBase


class TestHello(IntegrationTestBase):
    def test_hello(self):
        response = urllib.request.urlopen("http://localhost:5000/")
        result: str = response.read().decode()
        self.assertEqual("Hello World!", result)

    def test_callback(self):
        result = callback()
