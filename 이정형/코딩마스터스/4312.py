import sys

N, K = map(int, sys.stdin.readline().split())
MV = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
C = [int(sys.stdin.readline()) for _ in range(K)]
result = 0

MV.sort(key = lambda x: x[1], reverse = True)
C.sort()

for i in range(N):
  for j in C:
    if MV[i][0] <= j:
      result += MV[i][1]
      C.remove(j)
      break

print(result)