"""
This module contains functions to translate text between English and French using the MyMemoryTranslator.
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    This function takes a text in English and returns its translation in French.

    Parameters:
    english_text (str): The text in English to be translated.

    Returns:
    str: The translated text in French.
    """
    translator = MyMemoryTranslator(source="en", target="fr")
    french_text = translator.translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    This function takes a text in French and returns its translation in English.

    Parameters:
    french_text (str): The text in French to be translated.

    Returns:
    str: The translated text in English.
    """
    translator = MyMemoryTranslator(source="fr", target="en")
    english_text = translator.translate(french_text)
    return english_text
