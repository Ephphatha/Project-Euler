#! /usr/bin/python3

import unittest
from prime_factor import prime_factors

class TestPrimeFactor(unittest.TestCase):

  def test_prime(self):
    self.assertEqual(prime_factors(5), [5,])

  def test_composite(self):
    self.assertEqual(prime_factors(6), [2, 3,])

  def test_nonprime_noncomposite(self):
    self.assertFalse(prime_factors(1))

  def test_known(self):
    self.assertEqual(prime_factors(13195), [5, 7, 13, 29,])

if __name__ == "__main__":
  unittest.main()

