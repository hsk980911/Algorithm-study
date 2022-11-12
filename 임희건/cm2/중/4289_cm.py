# 유진이는 버스를 타고 병원에 가려고 합니다.
# 유진이가 살고있는 동네에는 N개의 버스 정류장과 M개의 버스 경로가 존재합니다.
# 버스 정류장에는 1번부터 N번까지 번호가 붙어있습니다.
# 버스 정류장과 버스 경로에 대한 정보가 주어질 때, 유진이의 집 근처 버스 정류장에서 출발해 병원 근처 버스 정류장까지 버스로 이동하는 데 걸리는 시간의 최솟값을 구하는 프로그램을 작성해주세요.

# 예제 입력1
# 5
# 7
# 1 2 4
# 1 3 2
# 1 4 6
# 2 3 3
# 2 4 4
# 3 5 3
# 4 5 5
# 2 5

# 예제 출력1
# 6

# 예제 입력2
# 4
# 5
# 1 2 7
# 1 3 2
# 2 3 3
# 2 4 9
# 3 4 6
# 1 4

# 예제 출력2
# 8

# 입력값 설명
# 첫째 줄에 버스 정류장의 개수 N이 주어집니다.
# N은 1 이상 5 이하의 양의 정수입니다.
# 둘째 줄에는 운행하는 버스 경로의 개수 M이 주어집니다.
# M은 1 이상 10 이하의 양의 정수입니다.
# 그리고 셋째 줄부터 M+2번째 줄까지 경로의 시작 정류장 번호 U, 경로의 도착 정류장 번호 V, 이동 시간 T가 주어집니다.
# 이는 U번 정류장에서 버스를 타서 V번 정류장까지 이동하는 데 T분이 걸린다는 의미입니다.
# M+3번째 줄에는 유진이의 집 근처 버스 정류장 번호 S와 병원 근처 버스 정류장 번호 E가 공백으로 구분되어 주어집니다.
# S에서 E로 이동할 수 없는 입력은 주어지지 않습니다.

# 출력값 설명
# 첫째 줄에 정답을 출력합니다.

import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
UVT = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
S, E = map(int, sys.stdin.readline().split())

UVT.sort(key=lambda x:x[2])
route = [S]
now = S
short = 0

while not S in route or not E in route:
    s = short
    s2 = short
    r = route.copy()
    r2 = route.copy()

    for uvt in UVT:
        if now in uvt[0:2] and E in uvt[0:2]:
            r.append(E)
            r = list(set(r))

            s += uvt[2]

            short = s
            route = r.copy()

            break

    if S in route and E in route:
        break

    for uvt in UVT:
        if now in uvt[0:2]:
            if uvt[0] in route or uvt[1] in route:
                if uvt[0] in route and uvt[1] in route:
                    pass

                else:
                    uvt2 = uvt[0:2]
                    uvt2.remove(now)
                    now = uvt2[0]

                    r2.append(uvt[0])
                    r2.append(uvt[1])
                    r2 = list(set(r2))

                    s2 += uvt[2]

                    UVT.remove(uvt)

                    break

    if s < s2 and E in r:
        short = s
        route = r.copy()

    else:
        short = s2
        route = r2.copy()

print(short)