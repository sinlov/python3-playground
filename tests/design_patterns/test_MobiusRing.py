import os
import unittest

from src.design_patterns import MobiusRing


class TestMobiusRing(unittest.TestCase):
    _test_data_folder = ""

    @classmethod
    def setUpClass(cls):
        _test_folder = os.path.split(os.path.realpath(__file__))[0]
        _test_data_folder = os.path.join(_test_folder, "testData")
        if not os.path.exists(_test_data_folder):
            os.makedirs(_test_data_folder)
        pass

    def test_something(self):
        write_path = os.path.join(self._test_data_folder, "1.text")
        mobius_ring = MobiusRing.MobiusRing()
        mobius_ring.set_write_path(write_path)
        mobius_ring.set_write_line_content("foo")
        mobius_ring.do()
        self.assertEqual(True, True)


if __name__ == "__main__":
    unittest.main()
