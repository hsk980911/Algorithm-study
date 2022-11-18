import sys
import math

A = int(sys.stdin.readline())

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return 0
    return 1

if A == 1:
  print(0)
else:
  print(is_prime_number(A))

