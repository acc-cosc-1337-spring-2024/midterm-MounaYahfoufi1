import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import unittest
from src.question_a.question_a import test_config as test_config_a, use_local_variable
from src.question_b.question_b import get_sum_of_evens
from src.question_c.question_c import get_fahrenheit
from src.question_d.question_d import use_global, global_var

class TestConfig(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config_a())

    def test_use_local_variable(self):
        num = 100
        use_local_variable(num)
        self.assertEqual(num, 100, "Expected 'num' to remain 100 after calling 'use_local_variable'.")

    def test_get_sum_of_evens_11(self):
        self.assertEqual(get_sum_of_evens(11), 30, "Expected sum of evens up to 11 to be 30")

    def test_get_sum_of_evens_10(self):
        self.assertEqual(get_sum_of_evens(10), 30, "Expected sum of evens up to 10 to be 30")

    def test_get_sum_of_evens_8(self):
        self.assertEqual(get_sum_of_evens(8), 20, "Expected sum of evens up to 8 to be 20")

    def test_get_fahrenheit_0(self):
        self.assertEqual(get_fahrenheit(0), 32, "Expected Fahrenheit equivalent of 0°C to be 32°F")

    def test_get_fahrenheit_5(self):
        self.assertEqual(get_fahrenheit(5), 41, "Expected Fahrenheit equivalent of 5°C to be 41°F")

    def test_get_fahrenheit_10(self):
        self.assertEqual(get_fahrenheit(10), 50, "Expected Fahrenheit equivalent of 10°C to be 50°F")

    def test_global_variable_modification(self):
        global global_var
        original_value = global_var
        use_global()
        self.assertNotEqual(original_value, global_var, "Expected global_var to be modified")
        self.assertEqual(global_var, 10, "Expected global_var to be changed to 10")
        global_var = original_value  

if __name__ == '__main__':
    unittest.main()




