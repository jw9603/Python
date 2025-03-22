# 백준 16236. 아기 상어
# https://www.acmicpc.net/problem/16236
import sys
from collections import deque
def bfs(x, y, shark_size, N, grid, directions):
    queue = deque([(x, y, 0)])
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True

    fish_list = []
    min_distance = float('inf')

    while queue:
        cur_x, cur_y, cur_d = queue.popleft()

        if 0 < grid[cur_x][cur_y] < shark_size:

            if cur_d < min_distance:
                min_distance = cur_d
                fish_list = [(cur_x, cur_y, cur_d)]
            elif cur_d == min_distance:
                fish_list.append((cur_x, cur_y, cur_d))
        
        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy

            if 0 <= next_x < N and 0 <= next_y < N:
                if grid[next_x][next_y] <= shark_size and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y, cur_d + 1))
    
    if fish_list:
        fish_list.sort()
        return fish_list[0]
    return None

def main():
    N = int(sys.stdin.readline().strip())

    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    shark_size = 2
    fish_eaten = 0
    time = 0

    for i in range(N):
        for j in range(N):
            if grid[i][j] == 9:
                shark_x, shark_y = i, j
                grid[i][j] = 0
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while True:
        result = bfs(shark_x, shark_y, shark_size, N, grid, directions)

        if not result:
            break

        shark_x, shark_y, move_time = result
        time += move_time

        grid[shark_x][shark_y] = 0
        fish_eaten += 1

        if fish_eaten == shark_size:
            shark_size += 1
            fish_eaten = 0

    print(time)

if __name__ == '__main__':
    main()