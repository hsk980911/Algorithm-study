from collections import Counter
import sys

cnt = int(sys.stdin.readline())
s_list = []

for i in range(cnt):
  s_list.append(int(sys.stdin.readline()))
s_list.sort()

def most_frequent(x):
  return max(x, key=x.count)

print(most_frequent(s_list))