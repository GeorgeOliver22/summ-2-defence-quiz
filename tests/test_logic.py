import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logic import validate_name, check_answer 

class TestQuizLogic(unittest.TestCase):

    def test_valid_name_standard(self):
        self.assertTrue(validate_name("Anonymous Person"))

    def test_valid_name_minimum_lenth(self):
        self.assertTrue(validate_name("Ap"))

    def test_name_too_short(self):
        self.assertFalse(validate_name("A"))

    def test_name_empty(self):
        self.assertFalse(validate_name(""))

    def test_check_answer_correct(self):
        self.assertTrue(check_answer("Official Sensitive", "Official Sensitive"))

    def test_check_answer_incorrect(self):
        self.assertFalse(check_answer("Official Sensitive", "SECRET"))     

if __name__ == "__main__":
    unittest.main()
