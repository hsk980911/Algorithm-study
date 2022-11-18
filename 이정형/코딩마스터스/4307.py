import sys

N, M = map(int, sys.stdin.readline().split())
P = [int(sys.stdin.readline()) for _ in range(N)]
p = 0
count = 0
# 작은거부터
P.sort(reverse = True)

for i in P:
  if p + i < M:
    p += i
    count += 1  
  

print(count)