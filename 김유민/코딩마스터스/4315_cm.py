# 4315 - 무향 그래프 2
import sys
n, m = map(int, sys.stdin.readline().split())
graph = [[]] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if graph[a] == []:
        graph[a] = [b]
    else: graph[a].append(b); graph[a].sort()
    if graph[b] == []:
        graph[b] = [a]
    else: graph[b].append(a); graph[b].sort()

graph.pop(0)
for g in graph:
    if g == []: print('no')
    else: print(*g, sep=' ')