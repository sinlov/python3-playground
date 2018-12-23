import unittest

from .design_patterns.mobius_ring_file import MobiusRing


class MyTestCase(unittest.TestCase):
    def test_something(self):
        MobiusRing().write_file('1.text', 'adadadad')
        MobiusRing().do()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
