# 11945 - 뜨거운 붕어빵
# 메모리: 30840KB, 시간: 68ms
import sys
n, m = map(int, sys.stdin.readline().split())
fish = []
for i in range(n):
    tmp = sys.stdin.readline().rstrip()
    fish.append(tmp[::-1])
print(*fish, sep='\n')