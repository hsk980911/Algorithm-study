def solution(sizes):
    answer = 0
    sum=[]
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
    for i in range(len(sizes)):
        sum.append(max(sizes)[0] * sizes[i][1])
    answer = max(sum)
            
    return answer