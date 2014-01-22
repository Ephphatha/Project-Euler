#! /usr/bin/python3

from math import factorial

def paths(n):
  return int(factorial(n+n)/(factorial(n)**2))

if __name__ == "__main__":
  print(paths(20))

