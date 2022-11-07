# 10816 - 숫자 카드 2
# 메모리: 114424KB, 시간: 848ms
import sys
from collections import Counter

_ = int(sys.stdin.readline())
n = map(int, sys.stdin.readline().split())
n_counter = Counter(n)      # 가지고 있는 숫자 카드의 숫자를 세어 딕셔너리 형태로 저장

_ = int(sys.stdin.readline())
m = map(int, sys.stdin.readline().split())
for i in m:                 # 찾아야 하는 숫자 카드의 개수 출력
    print(n_counter[i], end=' ')