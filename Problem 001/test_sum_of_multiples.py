#! /usr/bin/python

import unittest
from sum_of_multiples import *

class TestSumOfMultiples(unittest.TestCase):

  def test_sum_less_10_mult_3_5(self):
    self.assertEquals(sum_multiples([3,5,], 10), 23)

  def test_sum_less_5(self):
    self.assertEquals(sum_multiples([1,], 5), 10)

if __name__ == '__main__':
  unittest.main()

