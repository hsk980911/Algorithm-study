# 4320 - 깊이 우선 탐색
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[]] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if graph[a] == []:
        graph[a] = [b]
    else: graph[a].append(b); graph[a].sort()
    if graph[b] == []:
        graph[b] = [a]
    else: graph[b].append(a); graph[b].sort()

def DFS(graph, i, visited):
    visited[i] = True
    print(i, end=' ')
    for j in graph[i]:
        if not visited[j]:
            DFS(graph, j, visited)
            
DFS(graph, 1, visited)