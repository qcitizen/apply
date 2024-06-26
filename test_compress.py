import unittest
from compress import alphanumeric_compress

class TestAlphanumericCompress(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(alphanumeric_compress("aabbcc"), "a2b2c2")
        self.assertEqual(alphanumeric_compress("aaaaaffffffffffc"), "a5f10c")

    def test_empty(self):
        self.assertEqual(alphanumeric_compress(""), "")
    
    def test_single(self):
        self.assertEqual(alphanumeric_compress("a"), "a")
    
    def test_single_freq(self):
        self.assertEqual(alphanumeric_compress("abcd"), "abcd")

    def test_single_tail(self):
        self.assertEqual(alphanumeric_compress("aab"), "a2b")
    
    def test_numeric_ignore(self):
        self.assertEqual(alphanumeric_compress("a1b2c3"), "abc")
    
    def test_numeric_ignore_continue(self):
        self.assertEqual(alphanumeric_compress("effeac01cb65c"), "ef2eac2bc")
    
    def test_start_with_numeric(self):
        self.assertEqual(alphanumeric_compress("132134abc"), "abc")

    def test_only_numeric(self):
        self.assertEqual(alphanumeric_compress("123456"), "")

    def test_only_numeric_tail(self):
        self.assertEqual(alphanumeric_compress("abc123"), "abc")
    
    def test_upper(self):
        self.assertEqual(alphanumeric_compress("AABBCC"), "A2B2C2")


if __name__ == '__main__':
    unittest.main()


    
