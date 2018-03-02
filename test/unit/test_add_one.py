# -*- coding: utf-8 -*-
"""
Contains unit tests for :mod:`heating_controller.add_one`.
"""
import unittest
from heating_controller.add_one import add_one


class TestAddOne(unittest.TestCase):
    """
    Contains a unit test for adding one to a given function
    """
    def setUp(self):
        """
        This function contains setup code for the test. The method ``setUp``
        runs at the start of every test function. A test function
        is a function that either starts with the text ``test_`` or ends with
        the words ``_test``. ``unittest`` then runs the test, and reports if
        it passes.

        The analog of ``setUp`` is ``tearDown``, which runs after every test.
        ``tearDown`` does the required cleanup
        """
        self.expected_result_with_0 = 1
        self.expected_result_with_1 = 2

    def test_add_one_to_zero(self):
        """
        Tests that adding one to the number ``0`` returns a result of ``1``
        """
        self.assertEqual(self.expected_result_with_0, add_one(0))

    def test_add_one_to_one(self):
        """
        Tests that adding ``1`` to ``1`` returns a result of ``2``
        """
        self.assertEqual(self.expected_result_with_1, add_one(1))
