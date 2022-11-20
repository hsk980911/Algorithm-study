'''
dp로 풀수 있는데 그냥 board[][]자체에서 했다. 코드에 몇몇부분만 변경하면 dp로 되니 짜피 상관없을듯..

이렇게 되어 있으면 일단 board[i][j]가 0이면 정사각형이 성립이 안되니 1일 경우만 볼때

board[i-1][j-1], board[i-1][j], board[i][j-1] 중 최솟값과 1을 더해 정사각형 한 변의 길이의 합이 되도록 한다.

그다음에 구한 값중 제일 큰 값이 제일 큰 한변의 길이이므로 거기에 ^2를 해주면 정사각형의 넓이가 나오게 된다.
'''

def solution(board):
    answer = board[0][0]
    row = len(board)
    col = len(board[0])
    
    for i in range(1,row):
        for j in range(1,col):
            if board[i][j]==1:
                board[i][j] = 1+ min(board[i-1][j-1], board[i-1][j], board[i][j-1])
                answer = max(answer, board[i][j])
    
    return answer**2