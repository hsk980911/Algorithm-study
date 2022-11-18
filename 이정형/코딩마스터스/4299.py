import sys
from itertools import combinations

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

max_2 = list(combinations(num, 2))
max_3 = list(combinations(num, 3))

max2 = []
max3 = []
for item in max_2:
  max2.append(item[0] * item[1])
for item in max_3:
  max3.append(item[0] * item[1] * item[2])

print(max(max(max2), max(max3)))