# 빈동이는 동물원의 안전 책임자입니다. 동물원은 N행 M열의 격자, 총 N × M 칸으로 나눌 수 있습니다.
# 어느 날 재규어들이 우리에서 탈출했습니다.
# 이 재규어들은 매우 공격적이라 당장 포획할 수 없습니다.
# 빈동이는 입장객들에게 대피하라고 알린 뒤, 날뛰는 재규어를 막을 방법을 찾아냈습니다.
# 동물원은 빈 칸, 재규어가 있는 칸, 울타리가 있는 칸으로 구분할 수 있습니다.
# 재규어들은 상하좌우 중 한 방향으로 인접한 빈 칸으로 이동할 수 있으며, 동물원 밖으로 나가지 못합니다.
# 빈동이의 목표는 3개의 여분 울타리를 반드시 모두 설치해, 재규어가 도달할 수 없는 칸의 수를 최대화 하는 것입니다.
# 여분 울타리는 빈 칸에만 설치할 수 있고, 설치하면 그 칸은 울타리가 있는 칸이 됩니다.
# 빈동이가 목표를 달성했을 때, 재규어가 도달할 수 없는 빈 칸의 수를 출력하는 프로그램을 작성해주세요.

# 예제 입력1
# 4 4
# 0 1 0 0
# 1 0 2 0
# 0 1 0 0
# 0 0 1 1

# 예제 출력1
# 6

# 예제 입력2
# 6 4
# 1 1 0 1
# 2 1 1 1
# 1 2 2 0
# 0 1 1 0
# 2 0 1 1
# 1 0 1 2

# 예제 출력2
# 3

# 입력값 설명
# 첫째 줄에 동물원의 세로 크기 N과 가로 크기 M이 공백을 두고 주어집니다. (3 ≤ N, M ≤ 8)
# 둘째 줄부터 N+1째 줄까지, 각 줄에 공백으로 구분된 M개의 숫자로 동물원의 상태가 주어집니다.
# 0은 빈 칸, 1은 울타리가 있는 칸, 2는 재규어가 있는 칸입니다.
# 주어진 동물원의 상태에 빈 칸은 3개 이상, 재규어는 1마리 이상 존재함이 보장됩니다.

# 출력값 설명
# 3개의 울타리를 모두 설치한 뒤 재규어로부터 안전한 빈 칸의 개수의 최댓값을 출력합니다.

import sys
import numpy as np

def checking(n, m, j = [], z = []):
    x = j[0]
    y = j[1]

    z[x][y] = 2

    if x - 1 >= 0 and z[x - 1][y] == 0:
        z = checking(n, m, [x - 1, y], z)

    if x + 1 < n and z[x + 1][y] == 0:
        z = checking(n, m, [x + 1, y], z)

    if y - 1 >= 0 and z[x][y - 1] == 0:
        z = checking(n, m, [x, y - 1], z)

    if y + 1 < m and z[x][y + 1] == 0:
        z = checking(n, m, [x, y + 1], z)

    return z

N, M = map(int, sys.stdin.readline().split())
zoo = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
safe = []

jaguar = []

for i in range(N):
    for j in range(M):
        if zoo[i][j] == 2:
            jaguar.append([i, j])

zoo_flat = list(np.array(zoo).flatten())
zf = zoo_flat.copy()

for x in range(len(zoo_flat) - 2):
    if zoo_flat[x] == 0:
        zoo_flat[x] = 1

        for y in range(x + 1, len(zoo_flat) - 1):
            if zoo_flat[y] == 0:
                zoo_flat[y] = 1

                for z in range(y + 1, len(zoo_flat)):
                    if zoo_flat[z] == 0:
                        zoo_flat[z] = 1

                        zoo_rs = list(np.reshape(zoo_flat, (N, M)))

                        for a in range(N):
                            zoo_rs[a] = list(zoo_rs[a])

                        for ja in jaguar:
                            zoo_rs = checking(N, M, ja, zoo_rs)

                        s = 0

                        for a in zoo_rs:
                            s += a.count(0)

                        safe.append(s)

                        zoo_flat = zf.copy()

print(max(safe))