# 백준 13459. 구슬 탈출
# https://www.acmicpc.net/problem/13459
import sys
from collections import deque
def move(x, y, dx, dy, board):
    cnt = 0

    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def bfs(board, rx, ry, bx, by, N, M):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(rx, ry, bx, by, 0)])
    visited = set()
    visited.add((rx, ry, bx, by))

    while queue:
        rx, ry, bx, by, cur_t = queue.popleft()

        if cur_t >= 10:
            continue

        for dx, dy in directions:
            next_rx, next_ry, r_cnt = move(rx, ry, dx, dy, board)
            next_bx, next_by, b_cnt = move(bx, by, dx, dy, board)

            if board[next_bx][next_by] == 'O':
                continue
            if board[next_rx][next_ry] == 'O':
                return 1

            if (next_rx, next_ry) == (next_bx, next_by):
                if r_cnt > b_cnt:
                    next_rx -= dx
                    next_ry -= dy
                else:
                    next_bx -= dx
                    next_by -= dy
            
            if (next_rx, next_ry, next_bx, next_by) not in visited:
                visited.add((next_rx, next_ry, next_bx, next_by))
                queue.append((next_rx, next_ry, next_bx, next_by, cur_t + 1))
    
    return 0
            
def main():
    N, M = map(int, sys.stdin.readline().split())
    board = [list(sys.stdin.readline().strip()) for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                rx, ry = i, j
            elif board[i][j] == 'B':
                bx, by = i, j
    
    print(bfs(board, rx, ry, bx, by, N, M))

if __name__ == '__main__':
    main()