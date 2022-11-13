# 11655 - ROT13
# 메모리: 30840KB, 시간: 68ms

import sys
tmp=[]
S = sys.stdin.readline().rstrip()

for s in S:
    if s.islower():                     # 소문자
        t = chr(97+(ord(s)+13-97)%26) 
        tmp.append(t)
    elif s.isupper():                   # 대문자
        t = chr(65+(ord(s)+13-65)%26) 
        tmp.append(t)
    else: tmp.append(s)                 # 공백, 숫자, 특수문자 등
    
print(*tmp, sep='')