import sys
money, match = map(int, sys.stdin.readline().split())
match_li = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
cnt = 0
for i in match_li:
  if money - i < 0:
    continue
  money -= i
  cnt += 1
  
print(cnt)