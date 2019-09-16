""" Author: Michael Harmon
    Last Date Modified: 09/15/2019
    Description: These unit tests with test the average()
    from average_scores.py
    Update: Added two tests, 1 using mock to test negatives for average()
"""

import unittest
from unittest import mock
from validation_with_if import average_scores as av


class MyTestCase(unittest.TestCase):
    def test_average_positive(self):
        with mock.patch('builtins.input', side_effect=[85, 90, 95]):
            assert av.average() == 90

    def test_average_negative(self):
        with mock.patch('builtins.input', side_effect=[98, 93, 88]):
            assert av.average() != 91

    def test_average_string_raises_ValueError(self):
        with mock.patch('builtins.input', side_effect=['Test', 'Test', 'Test']):
            self.assertRaises(ValueError)

    def test_reject_negative_numbers(self):
        self.assertEqual(av.average(), -1)

    def test_reject_negative_values_using_mock(self):
        with mock.patch('builtins.input', side_effect=[-99, 99, 96]):
            self.assertEqual(av.average(), -1)


if __name__ == '__main__':
    unittest.main()

"""The unit tests ensured that the average method was actually returning the average.
    I added a positive test that returned the correct average and a negative test
    that would not return the correct average.
    This will ensure the average() method is calculating correctly.
"""
