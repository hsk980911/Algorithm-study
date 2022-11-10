'''
yellow의 크기와 brown의 크기를 더하면 전체 크기가 되고 
yellow의 크기는 (가로-2)*(세로-2)이며
brown의 크기는 전체 크기 - yellow의 크기가 된다.

for문을 이용해 가능한 가로, 세로의 크기를 구하고 if문으로 조건에 맞는 가로, 세로의 크기를 구한다.
'''

def solution(brown, yellow):
    answer = []
    
    s = brown + yellow
    
    for w in range(1,s):
        if s % w != 0:
            continue
        h = s//w
        y = (w-2)*(h-2)
        b = s-y
        if y == yellow and b == brown:
            if w<h:
                continue
            answer.append(w)
            answer.append(h)
    return answer