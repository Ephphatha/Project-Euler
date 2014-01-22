#! /usr/bin/python3

import string
from math import floor

def num2word(n):
  rep = ''

  if n > 999:
    rep = "{0} thousand".format(num2word(floor(n/1000)))
    n = n % 1000

  if n > 99:
    if rep:
      rep = "{0} {1} hundred".format(rep, num2word(floor(n/100)))
    else:
      rep = "{0} hundred".format(num2word(floor(n/100)))
    n = n % 100

  if n == 0:
    return rep or "zero"

  if n < 20:
    words = ["one", "two", "three", "four", "five", "six", "seven",
        "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",]
    if rep:
      rep = "{0} and {1}".format(rep, words[n-1])
    else:
      rep = words[n-1]
  else:
    tens = floor(n/10) - 2
    words = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty",
        "ninety"]
    n = n % 10

    tenword = words[tens]

    if n > 0:
      tenword = "{0}-{1}".format(tenword, num2word(n))

    if rep:
      rep = "{0} and {1}".format(rep, tenword)
    else:
      rep = tenword

  return rep

if __name__ == "__main__":
  cleanDict = {}

  for c in " -":
    cleanDict[ord(c)] = None

  print(sum([len(num2word(n).translate(cleanDict)) for n in range(1, 1001)]))

