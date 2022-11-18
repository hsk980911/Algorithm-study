import sys

N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
A = [a]

for i in range(N - 1):
    A.append(A[i][1:] + [A[i][0]])

for j in A:
    print(*j)