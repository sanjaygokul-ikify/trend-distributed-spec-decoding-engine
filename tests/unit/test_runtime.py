import unittest
from packages.core import SpeculativeDecodingException

class TestRuntime(unittest.TestCase):
    def test_speculative_decoding_exception(self):
        try:
            raise SpeculativeDecodingException('Test exception')
        except SpeculativeDecodingException as e:
            self.assertEqual(str(e), 'Test exception')

if __name__ == '__main__':
    unittest.main()
