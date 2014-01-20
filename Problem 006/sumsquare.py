#! /usr/bin/python3

if __name__ == "__main__":
  sumsquare, squaresum = 0, 0

  for x in range(1, 101):
    sumsquare += x * x
    squaresum += x

  squaresum *= squaresum

  print(squaresum - sumsquare)

