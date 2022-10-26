# 깊이 우선 탐색이란 그래프를 탐색(또는 순회)하는 방법 중 하나입니다. 
# 깊이 우선 탐색은 다음과 같은 방식으로 이루어집니다. 
# 1. 정점을 하나 정하여 방문하였다고 표시합니다. 
# 2. 이 정점과 간선으로 연결된 다른 정점에 대하여, 
# 2-1. 이미 방문했던 정점이라면 무시합니다. 
# 2-2. 아직 방문하지 않은 정점이라면 그 정점부터 다시 1을 적용합니다. 
# 이를 의사코드로 작성하면 다음과 같게 됩니다. 
# function DFS(V, E, C) {               // V : 정점의 집합, E : 간선의 집합, C : 현재 방문할 정점
#     visited[C] = true                 // 현재 정점을 방문하였다고 표시
#     for each x in E(C) {              // E(C) : C와 인접한 정점
#         if (!visited[x]) DFS(V, E, x) // 아직 방문하지 않은 정점이면 해당 정점부터 깊이 우선 탐색
#     }
# }
# 방향성과 가중치가 없는 그래프가 주어졌을 때 정점 1에서부터 깊이 우선 탐색을 수행하는 프로그램을 작성해주세요. 
# 탐색은 인접한 정점 중에서 정점번호가 작은 정점부터 수행합니다. 
# 정점의 개수가 N개일 때 각 정점의 번호는 1부터 N까지입니다.

# 예제 입력1
# 3 0

# 예제 출력1
# 1

# 예제 입력2
# 5 3
# 1 4
# 2 3
# 4 5

# 예제 출력2
# 1 4 5

# 입력값 설명
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 입력됩니다. (1 ≤ N, M ≤ 1,000)
# 둘째 줄부터 M + 1번째 줄까지 정수 A와 B가 입력됩니다. (1 ≤ A, B ≤ 1,000) 
# 이 때 각 줄은 A와 B가 서로 연결되었음을 의미합니다.

# 출력값 설명
# 정점 1에서 깊이 우선 탐색을 수행한 결과를 공백으로 구분하여 출력합니다.

import sys

def DFS(V, E, C):
    visited[C - 1] = True

    e = []

    for y in E:
        if C in y:
            y2 = y.copy()
            y2.remove(C)
            e.append(y2[0])

    e.sort()

    for x in e:
        if not visited[x - 1]:
            DFS(V, E, x)

N, M = map(int, sys.stdin.readline().split())

V = [i + 1 for i in range(N)]

E = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

visited = [False] * N

DFS(V, E, 1)

print(*[j + 1 for j in range(N) if visited[j]])