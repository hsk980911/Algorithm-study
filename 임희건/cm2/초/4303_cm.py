# 김 부장은 사업을 홍보하기 위해 경품 추첨 이벤트를 진행하려고 합니다.
# 이벤트 웹페이지의 URL이 있으면 사업 내용을 확인 후 경품 추첨에 참여할 수 있습니다.
# 우선 김 부장은 자신의 지인들에게 URL을 전송합니다.
# 김 부장에게 URL을 받은 지인들은 자신의 지인들에게도 URL을 전송합니다.
# 하지만 경품 추첨 참여자가 너무 많아지면 곤란하므로 참여 대상은 김 부장의 지인, 그리고 김 부장의 지인의 지인으로 한정하려고 합니다.
# 서로 지인 관계에 있는 사람들의 목록이 주어지면 경품 추첨에 참여할 수 있는 사람이 총 몇 명인지 출력하는 프로그램을 작성해주세요.
# 단, 경품 추첨에 김 부장은 참여하지 않으며 한 사람이 여러 번 참여할 수 없습니다.

# 예제 입력1
# 6 4
# 1 2
# 1 3
# 2 4
# 4 5

# 예제 출력1
# 3

# 예제 입력2
# 10 5
# 1 4
# 1 5
# 4 2
# 5 2
# 9 1

# 예제 출력2
# 4

# 입력값 설명
# 첫째 줄에 세상의 모든 사람 수 N(2 ≤ N ≤ 100)과 지인 관계의 수 M(1 ≤ M ≤ 1,000)이 공백을 구분으로 주어집니다.
# 둘째 줄부터 M개의 줄에 걸쳐 각 줄에 두 정수 a와 b가 공백을 구분으로 주어집니다. (a ≠ b, 1 ≤ a, b ≤ N)
# 이는 a번 사람과 b번 사람이 지인이라는 뜻이며 지인 관계는 항상 쌍방입니다.
# 즉, a번 사람이 b번 사람의 지인이라면 b번 사람도 a번 사람의 지인입니다.
# 같은 관계가 여러번 주어지지 않습니다.
# 특히 1번 사람은 김 부장입니다.

# 출력값 설명
# 경품 추첨에 참여할 수 있는 사람의 수를 출력합니다.

import sys

N, M = map(int, sys.stdin.readline().split())
AB = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
person = []
person2 = []

for i in AB:
    if 1 in i:
        x = i.copy()
        x.remove(1)
        person.append(x[0])

for j in person:
    for k in AB:
        if j in k and 1 not in k:
            y = k.copy()
            y.remove(j)

            if y[0] != 1 and y[0] not in person and y[0] not in person2:
                person2.append(y[0])

print(len(person) + len(person2))