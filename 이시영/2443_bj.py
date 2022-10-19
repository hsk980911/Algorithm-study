from sys import stdin

n = int(stdin.readline())

for i in range(n*2,0,-2):
    print(' '*(n-i//2)+'*'*(i-1))