# 4317 - 지방선거
import sys

n = int(sys.stdin.readline())
k = [0] * 1001
shoes_num = []
for i in range(n):
    shoes_num.append(int(sys.stdin.readline()))
for s in shoes_num:
    k[s] += 1
    
res = k[-1]
idx = 1000

for i, K in list(enumerate(k)):
    if K > res: res = K; idx = i
print(idx)