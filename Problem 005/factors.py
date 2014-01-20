#! /usr/bin/python3

import sys, os
sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../Problem 003')))

from itertools import *
from prime_factor import prime_factors

def factorise(n):
  if n < 1:
    return None

  factors = [1,]

  pfactors = [x for x in prime_factors(n)]
  pfactors = [x for x in chain.from_iterable(combinations(pfactors, r) for r in range(len(pfactors) + 1))]

  for comb in pfactors:
    product = 1
    for x in comb:
      product *= x
    if product not in factors:
      factors.append(product)

  return sorted(factors)

