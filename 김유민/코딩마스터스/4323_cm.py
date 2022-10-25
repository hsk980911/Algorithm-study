# 4323 - 데이트 자본주의
import sys

n, m = map(int, sys.stdin.readline().split())
p = list(map(int, sys.stdin.readline().split()))
p.sort(reverse=True)
res = []
for i in p:
    if i <= n:
        res.append(i)
        n -= i
print(len(res))