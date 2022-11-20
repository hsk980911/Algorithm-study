'''
문자열 슬라이싱을 통해 1,2,3,4... 씩 자르는데 어차피 자르는 가장 큰 경우는 전체길이의 절반의 개수가 되므로 len(s)//2+1을 해줘 시간을 단축시킨다. 

그다음 자른 문자열을 가지고 비교해 개수를 센다. 

ans는 현재 단위 문자열이 다음 문자열과 같으면 개수를 더해 다른 값이 나오면 그 더한 개수와 문자열을 더해 압축 문자열을 만든다.

압축 문자열의 길이들 중 작은 것을 골라 리턴하면 된다. 

여기서 위에 s의 길이가 1일때는 따로 if문으로 제한을 뒀다. 저렇게 안하면 테스트5번이 실패가 된다.
'''

def solution(s):
    answer=10000
    if len(s)==1:
        return 1
    for i in range(1, len(s)//2+1):
        b = ''
        count = 1
        ans=s[:i]
        for j in range(i, len(s)+i, i):
            if ans==s[j:i+j]:
                count+=1
            else:
                if count!=1:
                    b = b + str(count)+ans
                else:
                    b = b + ans
                ans=s[j:j+i]
                count = 1
        answer = min(answer, len(b))

    return answer