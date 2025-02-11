# 백준 2615. 오목
# https://www.acmicpc.net/problem/2615
import sys

board = [list(map(int, sys.stdin.readline().split())) for _ in range(19)]

# 방향 벡터 (오른쪽, 아래, ↘ 대각선, ↗ 대각선)
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

def check_winner(x, y, color):
    
    for i in range(4):
        count = 1
        nx, ny = x + dx[i], y + dy[i]
        
        while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == color:
            count += 1
            if count == 5:
                prev_x, prev_y = x - dx[i], y - dy[i]
                next_x, next_y = nx + dx[i], ny + dy[i]

                if 0 <= prev_x < 19 and 0 <= prev_y < 19 and board[prev_x][prev_y] == color:
                    break
                if 0 <= next_x < 19 and 0 <= next_y < 19 and board[next_x][next_y] == color:
                    break
                
                return color, x + 1, y + 1
            nx, ny = nx + dx[i], ny + dy[i]
    return None
        
            
def sol():
    for i in range(19):
        for j in range(19):
            if board[i][j] != 0:
                result = check_winner(i, j, board[i][j])
                if result:
                    print(result[0])
                    print(*result[1:])
                    return
    
    print(0)
    return

sol()
                