import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())
node_list = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
node_list.sort(key=lambda x: (x[0], x[1]))

graph = defaultdict(list)
for n, t in node_list:
  graph[n].append(t)

visited = [False] * N
def dfs_recursive(graph, start):
    if start in visited:
        return
    visited.append(start)
    print(start, end=' ')
    for now in graph[start]:
        dfs_recursive(graph, now)
        
dfs_recursive(graph, 1)
