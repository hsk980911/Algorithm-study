'''
처음에는 같은 열이 될때 0으로 해줘서 그 다음 크기가 max()값이 되도록 했는데 틀렸다.
생각해보니 극단적으로 다음 같은 열의 크기가 100이고 그 다음 크기가 7이되면 최고점이 될 수 없기 때문이다.

| 1 | 2 | 3 | 5 |
| 5 | 6 | 7 | 100 |
| 4 | 3 | 2 | 1 |
(이럴경우 안됨)

그래서 dp를 이용해 j가 같은 열이 될때의 이전 칸들의 해당 j값 제외 max()을 구해 land에 넣어줘 마지막 칸에 최고점을 구해준다.
'''

def solution(land):

#    coun=-1
#    for i in land:
#        if coun == i.index(max(i)):
#            i[i.index(max(i))]=0
#        answer+=max(i)
#        coun=i.index(max(i))

    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max(land[i-1][:j]+land[i-1][j+1:])
    print(land)
    return max(land[-1])