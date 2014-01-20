#! /usr/bin/python

import unittest
from sum_fibonacci import *

class TestSumFibonacci(unittest.TestCase):

  def test_first_term(self):
    self.assertEquals(fibonacci(2).next(), 1)

  def test_less_two(self):
    self.assertEquals(len([x for x in fibonacci(2)]), 2)

  def test_first_five_terms(self):
    self.assertEquals([x for (i, x) in enumerate(fibonacci(10)) if i < 5], [1, 1, 2, 3, 5])

if __name__ == "__main__":
  unittest.main()

