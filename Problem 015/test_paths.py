#! /usr/bin/python3

import unittest

from paths import paths

class TestPaths(unittest.TestCase):

  def test_n1(self):
    self.assertEqual(paths(1), 2)

  def test_n2(self):
    self.assertEqual(paths(2), 6)

if __name__ == "__main__":
  unittest.main()

