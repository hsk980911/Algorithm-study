# 일반적으로 두 소수의 곱을 A라고 할 때 A를 보고 역으로 두 소수를 유추해내는 것은 굉장히 어려운 것으로 알려져 있습니다.
# 이러한 성질은 암호학에서 다방면으로 활용되고 있습니다.
# 다만 두 소수의 곱 A가 충분히 크지 않은 숫자라면 역으로 두 소수를 유추해내는 것은 어려운 일이 아닙니다. 
# 어떠한 숫자 A가 주어졌을 때 두 소수의 곱으로 나타낼 수 있으면 두 소수를 오름차순으로 출력하고, 나타낼 수 없으면 IMPOSSIBLE을 출력하는 프로그램을 작성해주세요.

# 예제 입력1
# 15

# 예제 출력1
# 3 5

# 예제 입력2
# 20

# 예제 출력2
# IMPOSSIBLE

# 입력값 설명
# 첫째 줄에 정수 A가 주어집니다. (1 ≤ A ≤ 10,000,000)

# 출력값 설명
# 정수 A를 두 소수의 곱으로 나타낼 수 있으면 두 숫자를 오름차순으로 출력합니다. 
# 가능한 소수의 쌍이 많은 경우 가장 작은 소수와의 곱을 출력합니다.
# 만약 정수 A를 두 소수의 곱으로 나타낼 수 없다면 IMPOSSIBLE을 출력합니다.

import sys

def check(n, check):
    if n == 1:
        check = False

    elif n == 2:
        check = True

    else:
        for a in range(2, n):
            if n % a == 0:
                check = False
                break

    return check


A = int(sys.stdin.readline())

if A == 1:
    print('IMPOSSIBLE')

else:
    x, y = 0, 0
    check_x, check_y = True, True

    for i in range(2, A + 1):
        check_x, check_y = True, True

        if A % i == 0:
            x = i
            y = A // i

            check_x = check(x, check_x)
            check_y = check(y, check_y)
            
            if check_x and check_y:
                print(x, y)
                break

    if not check_x or not check_y:
        print('IMPOSSIBLE')