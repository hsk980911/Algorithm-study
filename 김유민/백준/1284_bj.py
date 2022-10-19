# 1284 - 집 주소
import sys

while True:
    n = sys.stdin.readline().rstrip()
    count = len(n)-1
    if n == '0': break
    for i in n:
        if i == '1': count+=2
        elif i == '0': count+=4
        else: count+=3
    count+=2
    print(count)