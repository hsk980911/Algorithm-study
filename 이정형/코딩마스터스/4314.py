import sys

N = int(sys.stdin.readline())
t = [0 for x in range(N)]

# 점화식 : DP[N] = DP[N-1] + 2 * DP[N-2]
t[0] = 1
t[1] = 3
for i in range(2, N):
  # 홀수 번째는 길이 1짜리 경우의 수 추가, 짝수 번째는 길이 2짜리 경우의 수 추가
  t[i] = (t[i-1] + 2 * t[i-2]) % 796796
print(t[N-1])