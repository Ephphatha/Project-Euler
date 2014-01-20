#! /usr/bin/python3

import unittest
from sieve import sieve

class TestSieve(unittest.TestCase):

  def test_invalidBounds(self):
    # 1 is not prime
    self.assertFalse([x for x in sieve(1)])

  def test_expected(self):
    # 2, 3 should both be reported as primes
    self.assertEqual([x for x in sieve(3)], [2,3,])

  def test_nonprimes_removed(self):
    # 4, 6 should be pruned as not a prime
    self.assertEqual([x for x in sieve(6)], [2,3,5])

  def test_long_list(self):
    integers = [x for x in sieve(60)]
    for i, x in enumerate(integers):
      for y in integers[i+1:]:
        self.assertFalse(y % x == 0, "{1} is not prime, divisible by {0}".format(x, y))

if __name__ == "__main__":
  unittest.main()

