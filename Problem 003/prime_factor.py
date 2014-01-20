#! /usr/bin/python3

from sieve import sieve

def prime_factors(n):
  '''Find the prime factors of N'''
  factors = []
  while n > 2:
    for p in sieve(n):
      if n % p == 0 or n == p:
        factors.append(p)
        n /= p
        break
  return factors

if __name__ == "__main__":
  print(max(prime_factors(600851475143)))

