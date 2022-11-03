# 식품 회사인 S기업은 창립 20주년을 맞이하여 서울역 앞에서 무료급식 행사를 진행하고 있습니다.
# 현재 N명의 사람이 배식을 받으러 줄을 서 있습니다.
# 기획팀 김 팀장은 배식 순서에 혼란이 오지 않게 다음의 기준에 따라 배식을 진행하려 합니다.
# 우선, 나이가 많은 사람부터 배식을 진행합니다.
# 나이가 같다면 먼저 온 사람 순서대로 진행합니다.
# 무료급식 행사가 성공적으로 진행되도록 배식 순서를 정해주는 프로그램을 작성해주세요.

# 예제 입력1
# 4
# 23 Seungkwan
# 23 Dongbin
# 22 Minkyu
# 24 Geonhyuk

# 예제 출력1
# Geonhyuk
# Seungkwan
# Dongbin
# Minkyu

# 예제 입력2
# 10
# 27 Hanul
# 32 Dongsu
# 45 Minsik
# 29 Dongsik
# 31 Jungsoon
# 39 Moonsik
# 59 Sanggeun
# 40 Oakseul
# 31 Misook
# 38 Taeil

# 예제 출력2
# Sanggeun
# Minsik
# Oakseul
# Moonsik
# Taeil
# Dongsu
# Jungsoon
# Misook
# Dongsik
# Hanul

# 입력값 설명
# 첫째 줄에 배식을 받으러 온 사람들의 수 N이 주어집니다. (1 ≤ N ≤ 100,000)
# 둘째 줄부터 N개의 줄에는 각 사람들의 나이와 이름이 공백으로 구분되어 주어집니다.
# 이 때 나이는 1보다 크거나 같으며, 150보다 작거나 같은 정수입니다.
# 또한 이름은 알파벳 대소문자로 이루어져 있고, 길이가 100보다 작거나 같은 문자열입니다.
# 입력은 먼저 온 순서로 주어집니다.

# 출력값 설명
# 기준에 따라 정렬된 이후의 사람들의 이름을 출력합니다.

import sys

N = int(sys.stdin.readline())
S = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
    S[i][0] = int(S[i][0])

S.sort(key = lambda x: x[0], reverse = True)

for j in range(N):
    print(S[j][1])