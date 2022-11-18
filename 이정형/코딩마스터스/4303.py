import sys

N, M = map(int, sys.stdin.readline().split())
AB = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
p = []
p2 = []

for i in AB:
    if 1 in i:
        x = i.copy()
        x.remove(1)
        p.append(x[0])

for j in p:
    for k in AB:
        if j in k and 1 not in k:
            y = k.copy()
            y.remove(j)

            if y[0] != 1 and y[0] not in p and y[0] not in p2:
                p2.append(y[0])

print(len(p) + len(p2))