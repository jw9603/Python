# 백준 17086. 아기 상어 2
# https://www.acmicpc.net/problem/17086
import sys
from collections import deque
def bfs(N, M, grid, directions):
    visited = [[False] * M for _ in range(N)]
    queue = deque()

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                queue.append((i, j, 0))
                visited[i][j] = True

    max_dist = 0

    while queue:
        cur_x, cur_y, cur_d = queue.popleft()

        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy

            if 0 <= next_x < N and 0 <= next_y < M:
                if not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    max_dist = max(max_dist, cur_d + 1)
                    queue.append((next_x, next_y, cur_d + 1))
    return max_dist

def main():
    N, M = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    print(bfs(N, M, grid, directions))

if __name__ == '__main__':
    main()