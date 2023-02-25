#!/usr/bin/env python

# webhook check comment - 1

import unittest
from unittest.main import main

from sort import sort

class TestSort(unittest.TestCase):
    def test_sort(self):
        self.assertEqual(sort([5,2,1,4,3]), [1, 2, 3, 4, 5])

    def test_sort_empty(self):
        self.assertEqual(sort([]), [])

    def test_sort_one(self):
        self.assertEqual(sort([1]), [1])



if  __name__ == '__main__':
    unittest.main()
