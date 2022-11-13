# 4316 - 무료급식
import sys

n = int(sys.stdin.readline())
st = []
for i in range(n):
    st.append(tuple(sys.stdin.readline().rstrip().split()))

st = sorted(st, key = lambda x: (-int(x[0])))

for i in st:
    print(i[1])