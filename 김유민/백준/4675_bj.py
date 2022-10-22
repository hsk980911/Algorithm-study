# 4675 - 셀프 넘버
# 메모리: 31860KB, 시간: 944ms

not_self_num = []
self_num = []

for i in range(1, 10001):
    i = str(i)
    self_num.append(i)          # self_num에 1부터 10000까지 append
    tmp = int(i)                # 숫자 자체를 tmp에 넣고
    for j in range(len(i)):     # 각 자릿수도 tmp에 더해줌
        tmp += int(i[j])
    tmp = str(tmp)
    not_self_num.append(tmp)    # 만들어진 수(tmp)는 셀프 넘버가 아니므로 not_self_num에 append

for i in range(1, 10001):
    i = str(i)
    if i in not_self_num:       # 숫자가 not_self_num에 있으면 self_num에서 해당 숫자를 지움
        self_num.remove(i)

print(*self_num, sep='\n')      # 셀프 넘버가 아닌 숫자만 남게 됨


# ------ 더 간단한 풀이 가능 ------
natural_num = set(range(1, 10001))
generated_num = set()

for i in range(1, 10001):       # i = 850       
    for j in str(i):            # j = "8", "5", "0"
        i += int(j)             # 850 + 8 + 5 + 0, i = 863
    generated_num.add(i)        # 생성자가 있는 숫자들

self_num = sorted(natural_num - generated_num)
print(*self_num, sep='\n')


'''
이렇게 하면 굳이 반복문 두 번 쓰지 않아도 됨 ㅜㅜ
'''