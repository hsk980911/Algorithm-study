import sys

N = int(sys.stdin.readline())
homes = []

for _ in range(N):
    homes.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, len(homes)):
    for j in range(len(homes[i])):
        if j == 0: homes[i][j] += min(homes[i-1][1], homes[i-1][2])
        elif j == 1: homes[i][j] += min(homes[i-1][0], homes[i-1][2])
        elif j == 2: homes[i][j] += min(homes[i-1][0], homes[i-1][1])
print(min(homes[-1]))