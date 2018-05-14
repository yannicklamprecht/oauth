from multiprocessing import Process
from unittest import TestCase

from oauth.src.server import app

server_process: Process


def start_test_server():
    app.run()


class IntegrationTestBase(TestCase):

    @classmethod
    def setUpClass(cls):
        global server_process
        server_process = Process(target=start_test_server)
        server_process.daemon = True
        server_process.start()

    @classmethod
    def tearDownClass(cls):
        global server_process
        server_process.terminate()
