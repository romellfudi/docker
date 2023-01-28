import unittest
from src.libs import generate_data, print_generated_data
# Write test case for method from libs.py 
class TestLibs(unittest.TestCase):
    def test_generate_data(self):
        # Write test case for generate_data
        df = generate_data(10)
        self.assertEqual(df.shape, (10, 2))
    def test_print_generated_data(self):
        # Write test case for print_generated_data, validate use print inside 
        df = generate_data(10)
        print_generated_data(df)
        self.assertEqual(df.shape, (10, 2))
        