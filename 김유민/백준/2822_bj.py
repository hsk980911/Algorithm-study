# 2822 - 점수 계산
# 메모리: 30840KB, 시간: 72ms

import sys
scores = []
for i in range(1, 9):
    scores.append(int(sys.stdin.readline()))

tmp = scores.copy()
tmp.sort(reverse=True)
tmp = tmp[:5]

order = []
for t in tmp:
    order.append(scores.index(t)+1)
order.sort()

print(sum(tmp))
print(*order)