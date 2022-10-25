import sys
num = int(input())
input_data = list(map(int, sys.stdin.readline().split()))
def second_largest_num(arr):
  unique_nums = set(arr)
  return sorted(unique_nums)[1]
if len(input_data) > 2:
  print(second_largest_num(input_data) * (num - 1))
elif len(input_data) <= 2:
  print(min(input_data) * num)