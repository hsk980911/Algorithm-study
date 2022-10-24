# 코딩테스트 출제 업무를 맡았던 또리는 문득 학생들의 코딩 성적이 궁금해졌습니다. 하지만 또리는 다른 업무로 몹시 바쁩니다.
# 또리를 위해 학생의 이름과 학생의 성적이 입력되면 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성해주세요.
# 이 때, 점수가 같은 학생이 있으면 사전순으로 앞서는 학생을 먼저 출력합니다.

# 예제 입력1
# 2
# Lucas 80
# Mason 77

# 예제 출력1
# Mason Lucas

# 예제 입력2
# 5
# John 50
# Henry 80
# Hena 30
# Kan 98
# Suji 58

# 예제 출력2
# Hena John Suji Henry Kan

# 입력값 설명
# 첫 번째 줄에 학생의 수 N이 입력됩니다. (1 ≤ N ≤ 100)
# 두 번째 줄부터 N + 1번째 줄에는 학생의 이름을 나타내는 문자열 A와 학생의 성적을 나타내는 정수 B가 공백을 기준으로 입력됩니다.
# 문자열 A는 알파벳 대소문자로 구성되어 있습니다.
# 문자열 A의 길이와 학생의 성적은 100 이하의 자연수입니다.

# 출력값 설명
# 모든 학생의 이름을 성적이 낮은 순서대로 공백으로 구분하여 출력합니다.
# 점수가 같은 학생이 있으면 사전순으로 앞서는 학생을 먼저 출력합니다.

import sys

N = int(sys.stdin.readline())
AB = []
A, B, S = [], [], []

for _ in range(N):
    a, b = map(str, sys.stdin.readline().split())
    AB.append([a, int(b)])

AB.sort()

for i in range(N):
    A.append(AB[i][0])
    B.append(AB[i][1])

for _ in range(N):
    S.append(A[B.index(min(B))])
    A.remove(A[B.index(min(B))])
    B.remove(min(B))

print(*S)