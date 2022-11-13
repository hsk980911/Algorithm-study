# 4324 - 분리수거장
import sys

n = int(sys.stdin.readline())
D, A = [], []
for i in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    D.append(x)
    A.append(y)

res = []
for i in range(len(D)):
    tmp = 0
    for ii, d in enumerate(D):
        tmp += abs((D[i] - d) * A[ii])
    res.append(tmp)\
    
print(res.index(min(res))+1)