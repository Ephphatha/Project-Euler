#! /usr/bin/python3

import unittest
import random
from divisible import isDivisible

class TestDivisible(unittest.TestCase):

  def test_divide_by_one(self):
    self.assertTrue(isDivisible(random.randint(1, 10), [1,]))

  def test_divide_by_self(self):
    x = random.randint(1, 10)
    self.assertTrue(isDivisible(x, [x,]))

  def test_multiplicand(self):
    x = random.randint(1, 10)
    self.assertTrue(isDivisible(x * random.randint(2, 10), [x,]))

  def test_multiple_factors(self):
    self.assertTrue(isDivisible(6, [2, 3,]))

  def test_non_factor(self):
    self.assertFalse(isDivisible(6, [2, 3, 4,]))

  def test_empty_divisors(self):
    with self.assertRaises(ValueError):
      isDivisible(4, [])

if __name__ == "__main__":
  unittest.main()

