'''
처음에 그냥 for문으로 풀었을 때 시간초과가 났었다. 그래서 dp로 누적합을 구했다.
dp를 구성할 때 자신 + 뒤 + 앞 - 곂치는 값해서 구성했고
결과값을 구할때 x,y의 값에서 i,j 값에 해당하는 값을 삭제한 후 i,j의 곂치는 값을 더했다.
'''

from sys import stdin

n, m = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().split()))for i in range(n)]
dp = [[0]*(m+1) for i in range(n+1)]
k = int(stdin.readline())

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = arr[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

for _ in range(k):
    i, j ,x, y = map(int, stdin.readline().split())
    print(dp[x][y] - dp[x][j-1]-dp[i-1][y] + dp[i-1][j-1])