#! /usr/bin/python3

if __name__ == "__main__":
  longest_chain = 1
  longest_start = 1

  known_lengths = [1]

  for start in range(2, 1000000):
    terms = 0
    n = start
    while n > len(known_lengths):
      terms += 1
      if n % 2 == 0:
        n = int(n / 2)
      else:
        n = int(3 * n + 1)

    terms += known_lengths[n - 1]
    known_lengths.append(terms)

    if terms > longest_chain:
      longest_chain = terms
      longest_start = start

  print(longest_start)

