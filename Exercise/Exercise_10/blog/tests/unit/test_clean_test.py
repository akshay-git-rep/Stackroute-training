import unittest
from clean_test import clean_text
 
class TestCleanText(unittest.TestCase):
    def test_basic_cleaning(self):
        input_text = "   This  Text  Needs  Cleaning  \n"
        expected_output = "this text neds cleaning"
        self.assertEqual(clean_text(input_text), expected_output)
 
    def test_empty_string(self):
        input_text = " HeLllooooo    "
        expected_output = "helo"
        self.assertEqual(clean_text(input_text), expected_output)
 