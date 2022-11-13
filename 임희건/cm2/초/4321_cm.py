# 학생 정보는 학생의 이름과 학생의 성적으로 구분됩니다.
# N개의 학생 정보가 주어졌을 때, 성적이 높은 순서대로 학생의 이름을 출력하는 프로그램을 작성해주세요.
# 단, 이름이 같은 학생이 존재할 수 있고, 점수가 같은 학생이 있으면 사전순으로 뒤에 오는 학생을 먼저 출력합니다.

# 예제 입력1
# 2
# Nadongbin 80
# Parkhanul 77

# 예제 출력1
# Nadongbin Parkhanul

# 예제 입력2
# 5
# John 50
# Henry 80
# Hena 30
# Kan 98
# Suji 58

# 예제 출력2
# Kan Henry Suji John Hena

# 입력값 설명
# 첫 번째 줄에 학생의 수 N이 입력됩니다. (1 ≤ N ≤ 100)
# 두 번째 줄부터 N + 1번째 줄에는 학생의 이름을 나타내는 문자열 A와 학생의 성적을 나타내는 정수 B가 공백을 기준으로 입력됩니다.
# 문자열 A는 1개 이상 100개 이하의 알파벳 소문자 또는 대문자로 구성되고, 학생의 성적은 100 이하의 양의 정수입니다.

# 출력값 설명
# 모든 학생들의 이름을 성적이 높은 순서대로 출력합니다.

import sys

N = int(sys.stdin.readline())
AB = []
A, B, S = [], [], []

for _ in range(N):
    a, b = map(str, sys.stdin.readline().split())
    AB.append([a, int(b)])

AB.sort(reverse = True)

for i in range(N):
    A.append(AB[i][0])
    B.append(AB[i][1])

for _ in range(N):
    S.append(A[B.index(max(B))])
    A.remove(A[B.index(max(B))])
    B.remove(max(B))

print(*S)