# 영현이는 몬스터 게임에 빠져 있습니다.
# 게임 속 주인공 레드는 이곳저곳을 돌아다니면서 몬스터들을 만나는 모험을 합니다.
# 레드는 게임 속 캐릭터이므로 상하좌우로만 움직일 수 있는데, 다양한 몬스터들을 만나러 맵의 모든 곳을 가보고 싶습니다.
# 하지만 육지와 육지 사이의 바다를 건너가야 할 때에는 날아가기 스킬을 사용해야 합니다.
# 물론 대각선으로는 움직일 수 없으므로 바로 대각선으로 이동하려는 경우에도 날아가기 스킬을 사용해야 합니다.
# 게임의 맵이 0과 1로 이루어진 M X N 형태로 주어지고, 육지가 1, 바다가 0이라고 가정할 때 레드가 날아가기 스킬을 몇번 사용해야 하는지 출력하는 프로그램을 작성해주세요.
# 캐릭터 레드가 처음에 등장할 위치를 결정하는 것도 날아가기 스킬을 한 번 사용하는 것으로 판단합니다.

# 예제 입력1
# 7 7 10
# 0 3
# 2 3
# 5 0
# 6 5
# 1 6
# 5 1
# 1 0
# 2 1
# 6 0
# 3 4

# 예제 출력1
# 8

# 예제 입력2
# 4 4 2
# 1 0
# 1 1

# 예제 출력2
# 1

# 입력값 설명
# 첫째 줄에는 맵의 가로길이 M(1 ≤ M ≤ 100)와 세로길이 N(1 ≤ N ≤ 100), 그리고 육지인 맵의 좌표의 개수 K(1 ≤ K ≤ 1,000)가 각각 공백을 두고 주어집니다.
# N, M, K는 모두 자연수입니다.
# 그 다음 K줄에는 육지인 곳의 곳의 좌표 X(0 ≤ X ≤ M - 1), Y(0 ≤ Y ≤ N - 1)가 각각 정수로 주어집니다.
# 육지가 아닌 곳의 좌표는 모두 바다입니다.

# 출력값 설명
# 레드가 맵의 모든 곳을 가보고자 할 때, 날아가기 스킬을 사용해야 하는 횟수를 출력합니다.

import sys
sys.setrecursionlimit(10000)

def checking(x, y, d = []):
    d[x][y] = 2

    if x - 1 >= 0 and d[x - 1][y] == 0:
        d = checking(x - 1, y, d)

    if x + 1 < N and d[x + 1][y] == 0:
        d = checking(x + 1, y, d)

    if y - 1 >= 0 and d[x][y - 1] == 0:
        d = checking(x, y - 1, d)

    if y + 1 < M and d[x][y + 1] == 0:
        d = checking(x, y + 1, d)

    return d

N, M, K = map(int, sys.stdin.readline().split())
land = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
skill = 0

map = [list([1] * M) for _ in range(N)]

for a in land:
    map[a[0]][a[1]] = 0

for i in range(N):
    for j in range(M):
        if map[i][j] == 0:
            map = checking(i, j, map)
            skill += 1

print(skill)