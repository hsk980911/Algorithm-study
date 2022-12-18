def solution(k, tangerine):
    tan_dict = {}  
    
    for i in range(len(tangerine)):
        if tangerine[i] not in tan_dict:
            tan_dict[tangerine[i]] = 1
        else:
            tan_dict[tangerine[i]] += 1
        
    
    tan_dict = sorted(tan_dict.items(), key=lambda x:x[1], reverse=True)
    
    cnt = 0
    for t in tan_dict:
        k -= t[1]
        cnt += 1
        if k <= 0:
            break
    return cnt