#! /usr/bin/python3

import sys, os
sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../Problem 003')))

from sieve import sieve

if __name__ == "__main__":
  for (i, v) in enumerate(sieve(sys.maxsize)):
    if i < 10000:
      continue
    print(v)
    break
