import sys

N = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))

sorted_score = score.copy()
sorted_score.sort(reverse=True)

for i in score:
    print(i, sorted_score.index(i) + 1)
