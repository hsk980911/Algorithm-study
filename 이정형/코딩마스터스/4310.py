import sys
sys.setrecursionlimit(100000)

M, N = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(M)]

def dfs(r, c):
    global cnt
    graph[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < M and 0 <= nc < N and graph[nr][nc] == 0:
            cnt += 1
            dfs(nr, nc)
            

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
cnt = 1
area = 0
ans = []

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            area += 1
            dfs(i, j)
            ans.append(cnt)
            cnt = 1
            
ans.sort()
print(area)
print(' '.join(map(str, ans)))