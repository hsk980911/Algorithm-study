# 4307 - 반품
import sys
n, m = map(int, sys.stdin.readline().split())
prices = []
for i in range(n):
    prices.append(int(sys.stdin.readline()))
prices.sort(reverse=True)

cnt, p = 0, 0
for _ in range(n):
    if p > m: break
    tmp = prices.pop(0)
    p += tmp
    if p > m: p -= tmp
    else: cnt+=1
print(cnt)