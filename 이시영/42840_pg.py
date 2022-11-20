'''
그냥 1번은 5씩, 2번은 8씩, 3번은 10씩 돌아가기때문에 그 숫자로 나눠 같으면 +1을 해준다. 
여기서 점수가 같을수있으니 a로 높은 수를 따로 빼줘 같다면 ans에 넣어주도록 했다.
'''

def solution(answers):
    answer = [0]*3
    ans=[]
    num1 = [1,2,3,4,5]
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if answers[i] == num1[i%5]:
            answer[0]+=1
        if answers[i] == num2[i%8]:
            answer[1]+=1
        if answers[i] == num3[i%10]:
            answer[2]+=1
    a = max(answer)
    for i in range(3):
        if a == answer[i]:
            ans.append(i+1)
        
    return ans