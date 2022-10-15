import sys
import decimal

T = int(sys.stdin.readline())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    
    d = ((x2-x1)**2 + (y2-y1)**2) ** (1/2)
    
    if d == 0 and r1 == r2:
        print(-1)
    elif r1+r2 == d or min(r1, r2)+d == max(r1, r2):
        print(1) 
    elif r1 + r2 > d and max(r1, r2) - min(r1, r2) < d:
        print(2)
    else:
        print(0)