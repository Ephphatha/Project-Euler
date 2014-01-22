#! /usr/bin/python3

import sys, os
sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../Problem 005')))

from factors import factorise

if __name__ == "__main__":
  i = 1
  tri = 0
  divisors = []

  while len(divisors) <= 500:
    tri += i
    divisors = factorise(tri)
    i += 1

  print(tri)

