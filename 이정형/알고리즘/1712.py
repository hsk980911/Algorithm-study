import sys
a, b, c = map(int, sys.stdin.readline().split())
# notebook = 0
# total = 0

# # 노트북 한 대 가격이 인건비보다 비싸면 어쨌든 손익분기점이 나타남
# if b > c:
#   notebook = -1
# else:
#   while total >= 0:
#     notebook += 1
#     total = a+(b*notebook) - c*notebook

# print(notebook)

# 시간 초과

if b >= c:
  print(-1)
else:
  # 생각해보면 1000만원에서 인건비 차액을 계속 빼는 방식
  print(int(a/(c-b)+1))