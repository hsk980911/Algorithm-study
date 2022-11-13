# 1260 - DFS와 BFS
# 메모리: 32476KB, 시간: 112ms
import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
graph = [[]] * (n+1)
visited = [False] * (n+1)

# 인접리스트 만들기
for _ in range(m):      
    v1, v2 = map(int, sys.stdin.readline().split())
    if graph[v1] == []:
        graph[v1] = [v2]
    else: 
        graph[v1].append(v2)
        graph[v1].sort()                # 번호가 작은 것 부터 순회해야 하므로 정렬 해준다.
    if graph[v2] == []:
        graph[v2] = [v1]
    else: 
        graph[v2].append(v1)
        graph[v2].sort()                # 번호가 작은 것 부터 순회해야 하므로 정렬 해준다.


# 깊이 우선 탐색 - 재귀 사용
def dfs(graph, i, visited):
    visited[i] = True
    print(i, end=' ')
    for j in graph[i]:
        if not visited[j]:              # 아직 방문하지 않은 정점에 대해 재귀
            dfs(graph, j, visited)

# 넓이 우선 탐색 - 큐 사용
def bfs(graph, i, visited):
    queue = deque()
    queue.append(i)                     # 큐에 시작 정점 삽입
    while queue:
        value = queue.popleft()         # FIFO
        if not visited[value]:          # 해당 정점이 아직 방문되지 않았다면
            print(value, end =' ')
            visited[value] = True
            for j in graph[value]:      # 연결된 정점을 큐에 삽입
                queue.append(j)   
            
dfs(graph, v, visited)

print()
visited = [False] * (n+1)
bfs(graph, v, visited)