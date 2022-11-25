x = input()
y = x
count = 0
while True:
    if int(y) < 10:
        y = '0' + y
    z = int(y[0]) + int(y[1])
    y = int(y[1] + str(z)[-1])
    y = str(y)
    count += 1
    if y == x:
        break
print(count)