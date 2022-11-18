import sys

N = int(sys.stdin.readline())

for i in range(2 ** N):
    n = bin(i)[2:].zfill(N)
    print(n)