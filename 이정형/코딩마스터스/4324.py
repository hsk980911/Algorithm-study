import sys
import copy

n = int(input())
x_y_list = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
distance_list = []
for a in x_y_list:
  temp_list = copy.copy(x_y_list)
  temp_list.remove(a)
  temp_distance = 0
  for aa in temp_list:
    temp_distance += abs(a[0] - aa[0]) * aa[1]
  distance_list.append(temp_distance)
  
print(distance_list.index(min(distance_list)) + 1)
