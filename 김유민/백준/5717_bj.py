# 5717 - 상근이의 친구들
# 메모리: 30840KB, 시간: 72ms
import sys

while True:
    m, f = map(int, sys.stdin.readline().split())
    if m==0 and f==0: break
    print(m+f)