import sys
a = sys.stdin.readline().upper()
b = list(a.rstrip('\n'))
# print(b)
word = list(set(b))
count_list =[]
# print(word)
for i in word:
    count = b.count(i)
    count_list.append(count)
#print(count_list)
if count_list.count(max(count_list)) >= 2:
    print('?')
else:
    find_index = count_list.index(max(count_list))
    print(word[find_index])