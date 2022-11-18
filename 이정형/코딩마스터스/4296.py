import sys

A, B = map(float, sys.stdin.readline().split())
result = []

while A <= B:
    result.append("{:.2f}".format(A))
    A = A + 0.01

print(*result)