import unittest

from faker import Faker


class TestFoo(unittest.TestCase):

    def test_user(self):
        self.assertEqual(True, True)
        self.assertGreater(1, 0)
        faker = Faker('zh_CN')
        self.assertNotEqual("", faker.name())
        pass
    pass