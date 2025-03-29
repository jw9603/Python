# 백준 1987. 알파벳
# https://www.acmicpc.net/problem/1987
import sys
def dfs(x, y, cnt):
    global max_cnt, R, C, board, directions, visited

    max_cnt = max(max_cnt, cnt)

    for dx, dy in directions:
        next_x, next_y = x + dx, y + dy

        if 0 <= next_x < R and 0 <= next_y < C:
            if board[next_x][next_y] not in visited:
                visited.add(board[next_x][next_y])
                dfs(next_x, next_y, cnt + 1)
                visited.pop()

def main():
    global max_cnt, R, C, board, directions, visited
    R, C = map(int, sys.stdin.readline().split())
    board = [list(sys.stdin.readline().strip()) for _ in range(R)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    max_cnt = 0
    visited = set()
    visited.add(board[0][0])

    dfs(0, 0, 1)
    print(max_cnt)

if __name__ == '__main__':
    main()