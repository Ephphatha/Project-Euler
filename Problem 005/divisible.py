#! /usr/bin/python3

from factors import factorise

import sys, os
sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../Problem 003')))

from sieve import sieve

def isDivisible(n, divisors):
  for x in divisors:
    if n % x != 0:
      return False

  if not divisors:
    raise ValueError("Must provide at least one divisor!")

  return True

if __name__ == "__main__":
  divisors = [x for x in range(20, 1, -1)]

  for x in divisors[:]:
    for y in factorise(x):
      if x != y and y in divisors:
        divisors.remove(y)

  prime_product = 1
  for x in sieve(max(divisors)):
    if x in divisors:
      prime_product *= x

  n = prime_product
  while not isDivisible(n, divisors):
    n += prime_product

  print(n)

