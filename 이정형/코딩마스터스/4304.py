import sys

A = int(sys.stdin.readline())

def is_prime(num, flag):
  if num == 1:
    flag = False
  elif num == 2:
    flag = True
  else:
    for i in range(2, num):
      if num % i == 0:
        flag = False
        break
  return flag

if A == 1:
  print('IMPOSSIBLE')
else:
  x = 0
  y = 0
  x_is_prime = True
  y_is_prime = True
  
  for i in range(2, A+1):
    x_is_prime, y_is_prime = True, True
    
    if A % i == 0:
      x = i
      y = A // i
      
      x_is_prime = is_prime(x, x_is_prime)
      y_is_prime = is_prime(y, y_is_prime)
      
      if x_is_prime and y_is_prime:
        print(x, y)
        break
  
  if not x_is_prime or not y_is_prime:
    print('IMPOSSIBLE')