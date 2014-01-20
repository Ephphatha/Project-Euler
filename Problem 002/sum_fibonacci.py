#! /usr/bin/python

def fibonacci(n):
  '''Generator that generates successive fibonacci terms until the value would
  exceed the given limit'''
  #previous and current term
  f0, f1 = 0, 1

  while f1 < n:
    yield f1
    f0, f1 = f1, f0+f1

if __name__ == "__main__":
  print sum([x for x in fibonacci(4000000) if x % 2 == 0])

