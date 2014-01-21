#! /usr/bin/python3

import math

if __name__ == "__main__":
  for a in range(1, 333):
    for b in range(a + 1, math.ceil((1000 - a) / 2)):
      c = 1000 - a - b
      if a*a + b*b == c*c:
        print(a*b*c)

