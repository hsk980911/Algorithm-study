# 태일이가 다니는 학교에는 얼마전 홍수가 크게 나서 길이 다 사라졌습니다.
# 대신 학교 건물들 중에서 몇몇 건물들은 서로 다리 하나로 연결되어 있다고 합니다.
# 연결이 되어 있는 건묻들끼리는 서로 왕래할 수 있습니다.
# 태일이는 조금 있으면 수업에 가야하는데 강의실까지 거리가 꽤 됩니다.
# 현재 태일이가 있는 건물에서 강의실까지 가장 빨리 갈 수 있게 도와주는 프로그램을 작성해주세요.

# 예제 입력1
# 4 3
# 1 2 2
# 2 3 5
# 3 4 7
# 4 2

# 예제 출력1
# 12

# 예제 입력2
# 5 8
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 1 5

# 예제 출력2
# 3

# 입력값 설명
# 첫째 줄에 학교 내 건물의 개수 N(1 ≤ N ≤ 100)과 다리의 개수 M(1 ≤ M ≤ 100,000)이 주어집니다.
# 둘째 줄부터 M + 1줄까지 처음에는 서로 연결되어 있는 건물들의 번호가 주어지고 이 건물들 사이를 오가는 데 걸리는 소요시간이 주어집니다.
# M + 2번째 줄에는 태일이가 현재 있는 건물의 번호와 가야하는 강의실의 건물 번호가 주어집니다.
# 소요 시간은 0보다 크고 100,000보다 작은 정수입니다.
# 또한, 도달할 수 없는 경우는 주어지지 않습니다.

# 출력값 설명
# 태일이가 강의에 가는 데에 걸리는 최소시간을 출력하세요.

import sys

N, M = map(int, sys.stdin.readline().split())
bridge = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
start, end = map(int, sys.stdin.readline().split())

bridge.sort(key=lambda x:x[2])
route = [start]
now = start
short = 0

while not start in route or not end in route:
    s = short
    s2 = short
    r = route.copy()
    r2 = route.copy()

    for b in bridge:
        if now in b[0:2] and end in b[0:2]:
            r.append(end)
            r = list(set(r))

            s += b[2]

            break

    for b in bridge:
        if now in b:
            if b[0] in route or b[1] in route:
                if b[0] in route and b[1] in route:
                    pass

                else:
                    b2 = b[0:2]
                    b2.remove(now)
                    now = b2[0]

                    r2.append(b[0])
                    r2.append(b[1])
                    r2 = list(set(r2))

                    s2 += b[2]

                    bridge.remove(b)

                    break

    if s < s2 and end in r:
        short = s
        route = r.copy()

    else:
        short = s2
        route = r2.copy()

print(short)