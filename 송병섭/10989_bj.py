import sys
a = int(input())
lst =[]
for i in range(a):
    lst.append(int(input()))
lst.sort()
for i in range(len(lst)):
    print(lst[i])