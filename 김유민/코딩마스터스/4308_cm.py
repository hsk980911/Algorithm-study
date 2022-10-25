# 4308 - 소수 판별
import sys, math

a = int(sys.stdin.readline())

def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False  
    return True

print(0 if a==1 else 1 if isPrime(a)==True else 0)