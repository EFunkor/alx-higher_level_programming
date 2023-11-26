#!/usr/bin/python3

import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Test cases for the max_integer function.
    """
    
    def test_empty_list(self):
        """
        Test max_integer with an empty list.
        """
        result = max_integer([])
        self.assertIsNone(result)

    def test_list_of_integers(self):
        """
        Test max_integer with a list of integers.
        """
        input_list = [1, 2, 3, 4, 5]
        result = max_integer(input_list)
        self.assertEqual(result, 5)

    def test_list_of_floats(self):
        """
        Test max_integer with a list of floats.
        """
        input_list = [1.1, 2.2, 3.3, 4.4, 5.5]
        result = max_integer(input_list)
        self.assertEqual(result, 5.5)

    def test_mixed_list(self):
        """
        Test max_integer with a mixed list of integers and floats.
        """
        input_list = [1, 2.2, 3.3, 4, 5]
        result = max_integer(input_list)
        self.assertEqual(result, 5.5)

if __name__ == '__main__':
    unittest.main()
