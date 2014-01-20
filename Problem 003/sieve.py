#! /usr/bin/python3
# Using the python generator described at the following url:
#  http://c2.com/cgi/wiki?SieveOfEratosthenesInManyProgrammingLanguages

def sieve(n):
  '''Generates prime numbers from 2 to N'''
  primes = {}
  
  p = 2

  while p <= n:
    if p not in primes:
      yield p
      primes[p * p] = [p]
    else:
      for p2 in primes[p]:
        primes.setdefault(p+p2, []).append(p2)
      del primes[p]
    p += 1

if __name__ == "__main__":
  print(sieve(1000))

