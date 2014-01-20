#! /usr/bin/python3

def isPalindrome(s):
  string = str(s)
  return string == string[::-1]

if __name__ == "__main__":
  max_palindromic_product = 0
  for x in range(999, 99, -1):
    for y in range(x, 99, -1):
      product = x * y
      if product > max_palindromic_product and isPalindrome(product):
        max_palindromic_product = product
  print(max_palindromic_product)

