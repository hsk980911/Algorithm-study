receipt_pay = int(input())
receipt_goods_cnt = int(input())

for i in range(receipt_goods_cnt):
  a, b = map(int, input().split())
  receipt_pay -= (a * b)
  
if receipt_pay == 0:
  print('Yes')
else:
  print('No')