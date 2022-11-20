# 이진수로 변환한 후 1의 개수가 같을때까지 더해준다.
def solution(n):
    answer = 0
    n_b = list(bin(n)[2:]).count('1')
    while True:
        
        if list(bin(n+1)[2:]).count('1') == n_b:
            answer=n+1
            break
        else:
            n+=1
    return answer