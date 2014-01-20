#! /usr/bin/python3

def isDivisible(n, divisors):
  for x in divisors:
    if n % x != 0:
      return False

  if not divisors:
    raise ValueError("Must provide at least one divisor!")

  return True

if __name__ == "__main__":
  x = 0
  divisors = range(1, 21)

  while True:
    x += 20
    if isDivisible(x, divisors):
      break
  print(x)

