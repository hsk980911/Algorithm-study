import sys
import heapq
import itertools

# num = int(input())
# input_data = list(map(int, sys.stdin.readline().split()))
# max_power = []
# nCr_list = []
# for i in range(num):
#   nCr = list(itertools.combinations(input_data, i+1))
#   nCr_list += nCr

# for power in nCr_list:
#   if len(power) < 2:
#     max_power.append(min(power))
#   else:
#     max_power.append(min(power)*(len(power)))

# print(max(max_power))
# 시간 초과
# ------------------------------------------------------------------------

num = int(input())
input_data = list(map(int, sys.stdin.readline().split()))

sorted_data = sorted(input_data, reverse=True)
temp_max = sorted_data[0]
idx = 1
for i in sorted_data:
  if temp_max < i * idx:
    temp_max = i * idx
  idx += 1
print(temp_max)