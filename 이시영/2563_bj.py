'''
처음에는 IoU를 생각했는데 사각형이 2개 이상이라 포기했다. 
그 다음에 생각한 것이 그냥 100으로 크기가 고정되어 있으니 
100,100의 크기를 가진 배열을 두고 넓이에 해당하는 것만 1를 해준다면 
중복도 생각안해도 되므로 이것으로 했다.
'''
from sys import stdin

n = int(stdin.readline())
ne=[]
for i in range(n):
    ne.append(list(map(int, stdin.readline().split())))
next = [[0]*101 for _ in range(101)]
for k in range(n):
    for i in range(ne[k][0],ne[k][0]+10):
        for j in range(ne[k][1], ne[k][1]+10):
            next[i][j]=1
count=0
for row in next:
    count+= row.count(1)
print(count)