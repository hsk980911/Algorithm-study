from itertools import permutations

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    arr = []
    
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            if ''.join(j)[0] != '0' and ''.join(j) != '1':
                arr.append(''.join(j))
    arr = list(set(arr))

    for i in arr:
        if is_prime(i) == True:
            answer += 1

    return answer

def is_prime(x):
    x = int(x)
    for i in range(2, int(x**0.5)+1):  
        if x % i == 0:     
            return False   
    return True