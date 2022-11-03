'''
그냥 아스키 코드 치환해서 푸는데 값이 z Z를 넘어가는 경우 -26을 해서 
a A로 돌아가게 했다.
'''
from sys import stdin

s = input()
for i in s:
    if i >='a' and i<='z':
        i = ord(i)+13
        if i >122:
            i-=26
        print(chr(i), end='')
    elif i >='A' and i <='Z':
        i = ord(i)+13
        if i >90:
            i-=26
        print(chr(i), end='')  
    else:
        print(i, end='')