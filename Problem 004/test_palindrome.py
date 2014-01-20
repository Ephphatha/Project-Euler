#! /usr/bin/python3

import unittest
import string
import random
from palindrome import isPalindrome

class TestPalindrome(unittest.TestCase):

  def test_single_chars(self):
    for c in string.ascii_letters:
      self.assertTrue(isPalindrome(c))

  def test_len_1_decimals(self):
    for i in range(10):
      self.assertTrue(isPalindrome(i))

  def test_even_length_strings(self):
    for c in string.ascii_letters:
      self.assertTrue(isPalindrome("{0}{0}".format(c)))
    for (c1, c2) in [(c1, c2) for c1 in string.ascii_letters for c2 in string.ascii_letters if c1 != c2]:
      self.assertFalse(isPalindrome("{0}{1}".format(c1, c2)))

  def test_odd_length_strings(self):
    for c in string.ascii_letters:
      self.assertTrue(isPalindrome("{0}{1}{0}".format(c, random.choice(string.ascii_letters))))
    for (c1, c2) in [(c1, c2) for c1 in string.ascii_letters for c2 in string.ascii_letters if c1 != c2]:
      self.assertFalse(isPalindrome("{0}{2}{1}".format(c1, c2, random.choice(string.ascii_letters))))

  def test_even_length_decimals(self):
    for i in range(1, 10):
      self.assertTrue(isPalindrome(i + 10 * i))
    for i in [x + 10 * y for x in range(10) for y in range(1, 10) if x != y]:
      self.assertFalse(isPalindrome(i), "{0} tested as a palindrome but shouldn't have (probably).".format(i))

  def test_odd_length_decimals(self):
    for i in range(1, 10):
      self.assertTrue(isPalindrome(i + 10 * random.randrange(10) + 100 * i))
    for i in [x + 10 * random.randrange(10) + 100 * y for x in range(10) for y in range(1, 10) if x != y]:
      self.assertFalse(isPalindrome(i), "{0} tested as a palindrome but shouldn't have (probably).".format(i))

if __name__ == "__main__":
  unittest.main()
