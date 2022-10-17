# 2083 - 럭비 클럽
# 메모리: 30840KB, 시간: 68ms

import sys

while True:
    name, age, weight = sys.stdin.readline().rstrip().split(' ')
    
    if name == '#' and age == '0' and weight == '0': break
    if int(age) > 17 or int(weight) >= 80: print(f'{name} Senior')
    else: print(f'{name} Junior')
    
'''
쉬어가는 문제,,,
'''