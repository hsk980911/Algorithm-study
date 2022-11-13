from sys import stdin

x, y = map(int, stdin.readline().split())

arr = sorted(list(map(int,stdin.readline().split())), reverse=True)
count=0
while arr:
    print(arr, x)
    if x-arr[0]>=0:
        x = x - arr[0]
        count+=1
        arr.pop(0)
    else:
        arr.pop(0)
print(count)