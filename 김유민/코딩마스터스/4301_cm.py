# 4301 - 반찬 투정
import sys
n = int(sys.stdin.readline())
num = list(i for i in range(2**n))
for i in num:
    print(bin(i)[2:].zfill(n))