import unittest

from src.bit_util.BitConverter import BitConverter


class BitConverterTest(unittest.TestCase):
    def test_is_big_endian(self):
        print("BitConverter.is_big_endian", BitConverter.is_big_endian())
        bool_true_byte = BitConverter.get_bytes_bool(True)
        if BitConverter.is_big_endian():
            self.assertEqual(b"\x10", bool_true_byte)
        else:
            self.assertEqual(b"\x01", bool_true_byte)
        bool_false_byte = BitConverter.get_bytes_bool(False)
        if BitConverter.is_big_endian():
            self.assertEqual(b"\x00", bool_false_byte)
        else:
            self.assertEqual(b"\x00", bool_false_byte)
        self.assertEqual(True, BitConverter.to_bool(bool_true_byte))
        self.assertEqual(False, BitConverter.to_bool(bool_false_byte))

    def test_converter_int(self):
        int_byte_3 = BitConverter.get_bytes_int(3)
        if BitConverter.is_big_endian():
            self.assertEqual(b"\x03\x00\x00\x00", int_byte_3)
        else:
            self.assertEqual(b"\x00\x00\x00\x03", int_byte_3)
        to_int = BitConverter.to_int(int_byte_3)
        self.assertEqual(3, to_int)

    def test_converter_short(self):
        data_byte = BitConverter.get_bytes_short(4)
        if BitConverter.is_big_endian():
            self.assertEqual(b"\x04\x00", data_byte)
        else:
            self.assertEqual(b"\x00\x04", data_byte)
        to_short = BitConverter.to_short(data_byte)
        self.assertEqual(4, to_short)

    def test_converter_str(self):
        self.assertEqual(
            b"\x61\x31\x30\x30\x30\x31", BitConverter.get_bytes_str_utf8(str("a10001"))
        )
        self.assertEqual(b"\x31\x30\x30\x30\x31", BitConverter.get_bytes_str_utf8(str("10001")))
        str_utf = BitConverter.get_bytes_str_utf8("abcdefg")
        self.assertEqual(b"\x61\x62\x63\x64\x65\x66\x67", str_utf)
        back = BitConverter.to_str_utf8(str_utf)
        self.assertEqual("abcdefg", back)


if __name__ == "__main__":
    unittest.main()
