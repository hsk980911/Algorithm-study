# 4318 - 전투력
import sys

n = int(sys.stdin.readline())
k = list(map(int, sys.stdin.readline().split()))
k.sort(reverse=True)
tmp = []

for i in range(n):
    tmp.append(k[i] * (i+1) )

print(max(tmp))