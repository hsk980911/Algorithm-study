import sys

N = int(sys.stdin.readline())
w = list(map(int, sys.stdin.readline().split()))
a, b = map(int, sys.stdin.readline().split())

w = w[a - 1:b]

print(min(w))