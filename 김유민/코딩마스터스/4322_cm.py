# 4322 - 성적이 낮은 순서대로 학생 출력하기
import sys

n = int(sys.stdin.readline())
st = []
for i in range(n):
    st.append(tuple(sys.stdin.readline().rstrip().split()))

st = sorted(st, key = lambda x: (x[1], x[0]))

for i in st:
    print(i[0], end=' ')