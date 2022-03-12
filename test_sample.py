"""
Test helper functions
"""

import unittest
from sample import increment_by_two, incremnt_by_three

class TestSampleMethods(unittest.TestCase):
    """
    Test harness
    """

    def test_increment_by_two(self):
        """
        Test increments
        """
        self.assertEqual(increment_by_two(-2), 0)
        self.assertEqual(increment_by_two(0), 2)
        self.assertEqual(increment_by_two(3), 5)
        
    def increment_by_three(var_to_increment):
        """
        This function increments input by three
        :param var_to_increment: param to increment
        :return: incremented variable
        """
        return var_to_increment + 3

if __name__ == '__main__':
    unittest.main()
