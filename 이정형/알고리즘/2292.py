num = int(input())

#  1 -> 6 -> 12 -> 18 -> 24 (6, 6, 6)
#  6개씩 증가
cnt = 1
num -= 1
if num == 0:
  print(cnt)
else:
  while (num - (6*cnt)) > 0:
    num -= 6*cnt
    cnt += 1
  cnt += 1
  print(cnt)

# while num > cnt:
#     cnt = cnt+6*i
#     i+=1
# print(i)
# if 굳이 안써도 됐네..