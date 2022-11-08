from sys import stdin

n = int(stdin.readline())
stdu = []
for i in range(n):
    a,b=input().split()
    stdu.append([a,int(b)])
    
stdu = sorted(stdu)
stdu = sorted(stdu, key=lambda x : x[1])
for i in stdu:
    print(i[0], end=" ")