# H대학교 컴퓨터교육과에서는 하반기 축제에서 외줄타기 이벤트를 진행합니다.
# 각 지점들끼리는 외줄로 연결되어 있고, 외줄을 타고 모든 지점을 통과하는 사람에게 상금으로 50만원을 수여하기로 했습니다.
# 모든 지점이 어떻게든 서로 도달할 수 있도록 구성되어 있으며 출발점은 본인이 정할 수 있습니다.
# 길이가 N인 외줄을 타는 데에 걸리는 시간은 N초입니다.
# 예를 들어 길이가 2인 외줄을 타는 데에는 2초가 걸립니다.
# 평소 승부욕과 재물욕이 많은 세아는 이번 이벤트에서 꼭 우승해서 상금을 타고 싶습니다.
# 세아를 위해 모든 지점을 통과할 수 있는 가장 짧은 시간을 구하는 프로그램을 작성해주세요.

# 예제 입력1
# 3 3
# 1 2 1
# 2 3 2
# 1 3 3

# 예제 출력1
# 3

# 예제 입력2
# 7 11
# 1 7 12
# 1 4 28
# 1 2 67
# 1 5 17
# 2 4 24
# 2 5 62
# 3 5 20
# 3 6 37
# 4 7 13
# 5 6 45
# 5 7 73

# 예제 출력2
# 123

# 입력값 설명
# 첫째 줄에 지점의 개수 V(1 ≤ V ≤ 10,000)와 외줄의 개수 E(1 ≤ E ≤ 100,000)가 주어집니다.
# 다음 E개의 줄에는 각 외줄에 대한 정보를 나타내는 세 정수 A, B, C가 주어집니다.
# 이는 A번 지점과 B번 지점이 길이가 C인 외줄로 연결되어 있다는 의미입니다. (1 ≤ A, B, C ≤ 10,000)

# 출력값 설명
# 첫째 줄에 모든 지점을 통과할 수 있는 가장 짧은 시간을 출력하세요.

import sys

V, E = map(int, sys.stdin.readline().split())
ABC = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]

ABC.sort(key=lambda x:x[2])

check = []
short = 0
abc = ABC.copy()
check.append(abc[0][0])
check.append(abc[0][1])
short += abc[0][2]
abc.remove(abc[0])

while len(check) < V:
    for rope in abc:
        if rope[0] in check or rope[1] in check:
            if rope[0] in check and rope[1] in check:
                abc.remove(rope)
                break

            else:
                check.append(rope[0])
                check.append(rope[1])
                check = list(set(check))
                short += rope[2]
                abc.remove(rope)
                break

print(short)