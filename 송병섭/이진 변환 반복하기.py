def solution(s):
    answer = []
    change = 0
    c_sum = 0
    while True:
        count = 0
        for i in range(len(s)):
            if s[i] == '0':
                count += 1
        c_sum+=count
        s=s.replace('0','')
        s=bin(len(s))[2:]
        change += 1
        if len(s) == 1:
            break
    answer.append(change)
    answer.append(c_sum)
    return answer