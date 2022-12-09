def solution(topping): 
    big = {i:0 for i in set(topping)}
    small = big.copy()
    
    for t in topping:
        small[t] += 1
    
    cnt_1 = 0
    cnt_2 = len(big)
    
    answer = 0
    
    for t in topping:
        if big[t] == 0:
            cnt_1 += 1
        if small[t] == 1:
            cnt_2 -= 1
        
        big[t] += 1
        small[t] -= 1
        
        if cnt_1 == cnt_2:
            answer += 1
    
    return answer 