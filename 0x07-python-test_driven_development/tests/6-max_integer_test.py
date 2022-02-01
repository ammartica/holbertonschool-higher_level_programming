#!/usr/bin/python3
"""Unittest for max_integer(list=[])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.Testcase):
    """unittest class for max_integer()"""
    def test_max_end(self):
        """Tests for max value at end of list"""
        e = [50, 9, 10, 39, 100]
        self.assertEqual(max_integer(e), 100)

    def test_max_beginning(self):
        """Tests for max value at start of list"""
        b = [100, 50, 8, 9, 39]
        self.assertEqual(max_integer(b), 100)

    def test_max_middle(self):
        """Tests for max value at middle of list"""
        m = [50, 9, 100, 34, 0]
        self.assertEqual(max_integer(m), 100)

    def test_one_negative(self):
        """Tests for max value in list with one negative"""
        on = [90, 7, -4, 100, 2]
        self.assertEqual(max_integer(on), 100)

    def test_all_negative(self):
        """Tests for max value in all negatives list"""
        an = [-90, -7, -4, -100, -2]
        self.assertEqual(max_integer(an), -2)

    def test_one_number(self):
        """Tests list with one value"""
        ov = [1]
        self.assertEqual(max_integer(ov), 1)

    def empty_list(self):
        """Tests empty list"""
        el = []
        self.assertIsNone(max_integer(el))

