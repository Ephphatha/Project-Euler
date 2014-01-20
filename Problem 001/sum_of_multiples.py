#! /usr/bin/python

def sum_multiples(multiples, n):
  '''Calculates the sum of numbers < N that are multiples of one of the numbers in
  the list Multiples'''

  total = 0
  for x in range(1, n):
    for y in multiples:
      if x % y == 0:
        total += x
        break

  return total

if __name__ == "__main__":
  print sum_multiples([3,5,], 1000)

