# 안전지대

def solution(board):

    n = len(board)
    # 위, 아래, 좌, 우,위 대각선, 아래 대각선
    dx = [-1,1,0,0,-1,-1,1,1] 
    dy = [0,0,-1,1,-1,1,-1,1]
    
    boom = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                boom.append((i,j))
    
    # 지뢰가 설치된 곳 주위에 폭탄 설치
    for x,y in boom:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < n:
                board[nx][ny] = 1
    cnt = 0
    for x in range(n):
        for y in range(n):
            if board[x][y] == 0:
                cnt += 1
    return cnt

if __name__ == '__main__':
    print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))
    print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]))
    print(solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]))