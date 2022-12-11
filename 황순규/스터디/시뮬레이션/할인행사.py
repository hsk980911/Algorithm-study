def solution(want, number, discount):
    wish_list = []
    for i in range(len(want)):
        wish_list.extend([want[i]]*number[i])
    print(wish_list)
        
    for i in range(len(discount) - 9):
        flag = 1
        temp = wish_list.copy()
        for j in discount[i:i+10]:
            if j not in temp:
                flag = 0
            else:
                temp.remove(j)
        if flag:
            return i
        else:
            return 0