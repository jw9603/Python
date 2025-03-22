# 백준 10026. 적록색약
# https://www.acmicpc.net/problem/10026
import sys
from collections import deque
def count_region(grid, N):
    visited = [[False] * N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                cnt += 1
                bfs(i, j, grid[i][j], visited, grid, N)

    return cnt

def bfs(x, y, color, visited, grid, N):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        cur_x, cur_y = queue.popleft()

        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy

            if 0 <= next_x < N and 0 <= next_y < N:
                if not visited[next_x][next_y] and grid[next_x][next_y] == color:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y))

def main():
    N = int(sys.stdin.readline().strip())
    grid = [list(sys.stdin.readline().strip()) for _ in range(N)]

    normal_cnt = count_region(grid, N)

    blind_grid = [['G' if grid[i][j] == 'R' else grid[i][j] for j in range(N)] for i in range(N)]

    blind_cnt = count_region(blind_grid, N)

    print(normal_cnt, blind_cnt)

if __name__ == '__main__':
    main()