import sys

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N)]

# i 번째 행의 합 = i 번째 열의 합 = Vi의 차수
# 인접 리스트
for _ in range(M):
  a, b = map(int, sys.stdin.readline().split())
  graph[a - 1].append(b)
  graph[b - 1].append(a)
  
for x in graph:
  if x:
    x.sort()
    
for x in graph:
  if x:
    print(*x)
  else:
    print('no')