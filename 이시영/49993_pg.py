'''
스킬트리의 값을 하나씩 스킬의 값과 비교하면서 있다면 s에 넣어 최종적으로 
완성된 s가 선행 스킬 순서에 맞는지 확인해 맞으면 answer을 +1한다.
'''
def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        s=''
        for j in i:
            if j in skill:
                s+=j
        if skill[:len(s)] == s:
            answer+=1
    return answer