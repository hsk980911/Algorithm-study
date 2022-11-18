import sys

N = int(sys.stdin.readline())
A = [int(sys.stdin.readline()) for _ in range(N)]
B, C = map(int, sys.stdin.readline().split())
count = 0

for i in A:
    if B > C:
        i = i - B
        count += 1
        
    if i > 0:
        count += i // C

        if i % C > 0:
            count += 1

print(count)