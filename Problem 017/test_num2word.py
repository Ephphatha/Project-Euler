#! /usr/bin/python3

import unittest

from num2word import num2word

class TestNum2Word(unittest.TestCase):

  def test_zero(self):
    self.assertEqual(num2word(0), "zero")

  def test_ones(self):
    self.assertEqual(num2word(5), "five")

  def test_teens(self):
    self.assertEqual(num2word(13), "thirteen")

  def test_tens(self):
    self.assertEqual(num2word(40), "forty")

  def test_tens_and_one(self):
    self.assertEqual(num2word(42), "forty-two")

  def test_hundred(self):
    self.assertEqual(num2word(200), "two hundred")

  def test_hundred_and_ones(self):
    self.assertEqual(num2word(605), "six hundred and five")

  def test_hundred_and_tens(self):
    self.assertEqual(num2word(730), "seven hundred and thirty")

  def test_hundred_tens_and_ones(self):
    self.assertEqual(num2word(824), "eight hundred and twenty-four")

  def test_thousands(self):
    self.assertEqual(num2word(1000), "one thousand")

if __name__ == "__main__":
  unittest.main()

