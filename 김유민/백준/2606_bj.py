# 2606 - 바이러스
# 메모리: 30840KB, 시간: 68ms
import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[]] * (n+1)
visited = [False] * (n+1)
tmp = []

for _ in range(m):
    v1, v2 = map(int, sys.stdin.readline().split())
    if graph[v1] == []:
        graph[v1] = [v2]
    else: graph[v1].append(v2)
    if graph[v2] == []:
        graph[v2] = [v1]
    else: graph[v2].append(v1)
    
# DFS로 풀이 - 재귀 사용
def virus(graph, i, visited):
    visited[i] = True
    tmp.append(i)                       # 바이러스에 걸리는 컴퓨터를 tmp에 저장
    for j in graph[i]:
        if not visited[j]:
            virus(graph, j, visited)

virus(graph, 1, visited)
print(len(tmp)-1)                       # 1번 컴퓨터는 제외해야 하므로 -1