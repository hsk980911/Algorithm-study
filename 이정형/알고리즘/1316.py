from itertools import groupby
from collections import Counter

cnt = int(input())
group_list = []
group_cnt = 0
for i in range(cnt):
  temp = input()
  temp_group_list = [k for k, g in groupby(temp)]
  counter = Counter(temp_group_list)
  result = list(counter.values())
  if max(result) == 1:
    group_cnt += 1


print(group_cnt)


# result = 0
# for i in range(int(input())):
#     word = input()
#     if list(word) == sorted(word, key=word.find):
#         result += 1
# print(result)

# 일단 문자열 리스트로 만들면 사전 순으로 정렬
# key를 단어의 find를 먹여주면 사전순으로 중복되게 나열
# 그게 list(word)랑 같으면 중복되는게 없는거니까.,.. 근데 이건 딱 맞딱뜨리면 절대 생각 못할 듯