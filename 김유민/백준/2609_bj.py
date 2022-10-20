# 2609 - 최대공약수와 최소공배수
# 메모리: 32952KB, 시간: 76ms

import math, sys

n, m = map(int, sys.stdin.readline().split())
print(math.gcd(n, m), math.lcm(n, m), sep='\n')  # math 라이브러리를 통해 쉽게 구할 수 있음