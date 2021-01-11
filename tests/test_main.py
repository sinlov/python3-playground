import unittest
import os


class TestMain(unittest.TestCase):
    def test_print_evn(self):
        env_http_port = os.getenv('ENV_HTTP_PORT')
        print('env: ENV_HTTP_PORT=%s' % env_http_port)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
