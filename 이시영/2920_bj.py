from sys import stdin

n = list(map(int,stdin.readline().split()))
ch = [1, 2, 3, 4, 5, 6, 7, 8]
if n == ch:
    print('ascending')
elif n == ch[::-1]:
    print('descending')
else:
    print('mixed')