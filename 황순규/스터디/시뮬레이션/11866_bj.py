import sys
from collections import deque

N, k = map(int, sys.stdin.readline().split())

dq = deque(range(1, N+1))

cnt = 0
strings = '<'
while dq:
    if len(dq) == 1:
        strings += str(dq.popleft())
        break
    cnt += 1
    if cnt % k == 0:
        strings += str(dq.popleft()) + ', '
    else:
        dq.append(dq.popleft())
strings += '>'

print(strings)