import sys
num = int(sys.stdin.readline())
p_list = []

for i in range(num):
  p_list.append(list(map(str, sys.stdin.readline().split())))

p_list.sort(key=lambda x:x[0], reverse=True)

for p in p_list:
  print(p[1])