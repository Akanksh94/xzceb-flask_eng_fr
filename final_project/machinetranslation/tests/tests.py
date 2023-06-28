from machinetranslation import translator
import unittest

class TestTranslator(unittest.TestCase):

    
    def test_english_to_french_hello(self):
        self.assertEqual(translator.english_to_french('hello'), 'bonjour')
        self.assertNotEqual(translator.english_to_french('hello'), 'hello')
    
    def test_french_to_english_bonjour(self):
        self.assertEqual(translator.french_to_english('bonjour'), 'hello')
        self.assertNotEqual(translator.french_to_english('bonjour'), 'bonjour')

if __name__ == '__main__':
    unittest.main()
