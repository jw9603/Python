# 백준 1987. 알파벳
# https://www.acmicpc.net/problem/1987
import sys
def dfs(x, y, count):
    global max_cnt, directions, R, C, board, visited
    max_cnt = max(max_cnt, count)

    for dx, dy in directions:
        next_x, next_y = x + dx, y + dy

        if 0 <= next_x < R and 0 <= next_y < C:
            if board[next_x][next_y] not in visited:
                visited.add(board[next_x][next_y])
                dfs(next_x, next_y, count + 1)
                visited.remove(board[next_x][next_y])

def main():
    global max_cnt, directions, R, C, board, visited
    R, C = map(int, sys.stdin.readline().split())
    board = [list(sys.stdin.readline().strip()) for _ in range(R)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    max_cnt = 0

    visited.add(board[0][0])
    dfs(0, 0, 1)
    print(max_cnt)

if __name__ == '__main__':
    main()