import sys
score_li = []
for i in range(int(input())):
  input_data = sys.stdin.readline().split()
  score_li.append((input_data[0], int(input_data[1])))

score_li = sorted(score_li)
score_li = sorted(score_li, key=lambda x:x[1])
for i in score_li:
  print(i[0], end=' ')