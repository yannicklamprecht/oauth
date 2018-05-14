import urllib.request

from oauth.tests.integration_test_base import IntegrationTestBase


class TestHello(IntegrationTestBase):
    def test_hello(self):
        response = urllib.request.urlopen("http://localhost:5000/")
        result: str = response.read().decode()
        self.assertEqual("Hello World!", result)
