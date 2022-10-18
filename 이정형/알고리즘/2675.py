cnt = int(input())
result = []
for i in range(cnt):
  temp = ''
  a, b = input().split()
  for s in b:
    temp += (s * int(a))
  result.append(temp)
  
for s in result:
  print(s)