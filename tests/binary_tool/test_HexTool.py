import unittest

from src.binary_tool import HexTool


class HexToolTests(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.test_str = "12345678qwertyui"
        self.test_hex_str = "31323334353637387177657274797569"

    def test_bytes_to_hex_str(self):
        str_to_bytes = HexTool.str_to_bytes(self.test_str)
        hex_str = HexTool.bytes_to_hex_str(str_to_bytes)
        print(f"HexTool.bytes_to_hex_str {hex_str}")
        self.assertEqual(self.test_hex_str, hex_str)

    def test_hex_str_to_bytes(self):
        to_bytes = HexTool.hex_str_to_bytes(self.test_hex_str)
        to_str = HexTool.bytes_to_str(to_bytes)
        print(f"HexTool.bytes_to_str {to_str}")
        self.assertEqual(self.test_str, to_str)


if __name__ == "__main__":
    unittest.main()
