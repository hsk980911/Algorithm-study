'''
순열을 이용해 던전 탐험의 순서를 전부 구한다. 
여기서 go함수는 유저가 탐험할 수 있는 던전 수를 구하는 함수로 순열을 이용해 구한 탐험 순서대로 go함수에 넣어 최대 던전 수를 구하도록 했다.
'''

from itertools import permutations
def go(dungeons, k):
    count=0
    for i in dungeons:
        if i[0] > k:
            continue
        else:
            k-=i[1]
            count+=1
    return count

def solution(k, dungeons):
    answer = -1
    count=[]
    a = list(permutations(dungeons,len(dungeons)))
    for i in a:
        count.append(go(i,k))
    return max(count)