#! /usr/bin/python3

import unittest
from factors import factorise

class TestFactors(unittest.TestCase):

  def test_one(self):
    self.assertEqual(factorise(1), [1,])

  def test_two(self):
    self.assertEqual(factorise(2), [1,2])

  def test_composite(self):
    self.assertEqual(factorise(6), [1,2,3,6])

  def test_square(self):
    self.assertEqual(factorise(4), [1,2,4])

if __name__ == "__main__":
  unittest.main()

