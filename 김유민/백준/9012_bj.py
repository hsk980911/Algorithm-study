# 9012 - 괄호
# 메모리: 30840KB, 시간: 76ms

import sys
n = int(sys.stdin.readline())

for i in range(n):
    flag ='YES'
    ps = list(sys.stdin.readline().rstrip())
    check = []
    
    for i in range(len(ps)):
        if ps[i] =='(': check.append(ps[i])     # 왼쪽 괄호이면 스택에 추가
        elif ps[i] == ')':
            try: check.pop()                    # 스택에 아무것도( '(' ) 없는데 ')'가 들어올 경우 error 발생
            except: flag='NO'                   # 짝이 맞지 않는다는 의미이므로 예외처리
                                                # 짝이 맞는 경우는 flag(=YES)가 바뀌지 않음
            
    if len(check)!=0: flag='NO'                 # 스택에 왼쪽 괄호가 남아있는 경우 짝이 맞지 않는다는 의미이므로 flag=NO
    print(flag)
    