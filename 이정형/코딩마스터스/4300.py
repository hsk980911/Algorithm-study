import sys

A, B = map(int, sys.stdin.readline().split())
N, M = map(int, sys.stdin.readline().split())
money = [int(sys.stdin.readline()) for _ in range(N)]

money.sort(reverse = True)

result = sum(money[0:M])

print(A + B * result)