# 4470 - 줄번호
# 메모리: 30840KB, 시간: 68ms

import sys

input = sys.stdin.readline
n = int(input())
arr = []

for i in range(n):
    arr.append(input().rstrip())
for i, a in enumerate(arr):
    print(f'{i+1}. {a}')