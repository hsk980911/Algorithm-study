import sys
from collections import defaultdict

N = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))
d = [x for x in range(1, 11)]

li = sorted(list(zip(M, d)), key=lambda x: x[0])
depth_list = [0]
graph = defaultdict(list)
for n, t in li:
  graph[n].append(t)
def dfs(v, depth, discovered=[]):
    discovered.append(v) # discovered는 탐색한 노드들을 저장한다.
    for w in graph[v]:
        if not w in discovered: # w가 탐색한 노드가 아니라면 탐색한다.
            depth_list.append(depth)
            discovered=dfs(w,depth+1,discovered) 
    return discovered

result = dict(zip(dfs(1, 1), depth_list))
result_list = [result[x] for x in range(1, N+1)]

print(max(result_list))
