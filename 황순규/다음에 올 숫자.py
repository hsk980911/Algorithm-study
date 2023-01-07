def solution(common):
    answer = 0
    temp = common[1] - common[0]
    if common[2] - common[1] == temp:
        return common[-1] + temp
    else:
        temp = int(common[1] // common[0])
        return common[-1] * temp
