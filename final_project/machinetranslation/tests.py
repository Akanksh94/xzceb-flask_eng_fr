import translator
import unittest

class TestTranslator(unittest.TestCase):

    
    def test_english_to_french_hello(self):
        self.assertEqual(translator.english_to_french('hello'), 'bonjour')

    
    def test_french_to_english_bonjour(self):
        self.assertEqual(translator.french_to_english('bonjour'), 'hello')


if __name__ == '__main__':
    unittest.main()
