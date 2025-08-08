import unittest
from hello import get_random_quote

class TestHello(unittest.TestCase):
    def test_get_random_quote(self):
        quote = get_random_quote()
        self.assertIsInstance(quote, str)
        self.assertGreater(len(quote), 0)

if __name__ == '__main__':
    unittest.main()