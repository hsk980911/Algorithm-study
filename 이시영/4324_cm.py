from sys import stdin

n = int(stdin.readline())
apart=[]
for i in range(n):
    apart.append(list(map(int, stdin.readline().split())))
a=[]
for i in range(n):
    amin=0
    for j in range(n):
        amin +=abs((apart[i][0]-apart[j][0])*apart[j][1])
    a.append(amin)
print(a.index(min(a))+1)