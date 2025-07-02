# 백준 2589. 보물섬
# https://www.acmicpc.net/problem/2589
############################# 문제 이해 #############################
# 보물섬 지도는 직사각형 모양이며 여러 칸으로 나뉘어져 있다. 각 칸은 육지(L)나
# 바다(W)로 표시되어 있다.
# 이 지도에서 이동은 상하좌우로 이웃한 육지로만 가능하며, 한 칸 이동하는 데 한 시간이 걸림
# 보물은 서로 간에 최단 거리로 이동하는 데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어
# 묻혀있음.
############################# 문제 이해 #############################
from collections import deque
def bfs(x, y, grid, N, M, directions):
    queue = deque([(x, y, 0)])
    visited = [[False] * M for _ in range(N)]
    visited[x][y] = True

    max_dist = 0

    while queue:
        cur_x, cur_y, cur_t = queue.popleft()
        max_dist = max(cur_t, max_dist)

        for dx, dy in directions:
            nx, ny = cur_x + dx, cur_y + dy

            if 0 <= nx < N and 0 <= ny < M:
                if grid[nx][ny] == 'L' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, cur_t + 1))
    
    return max_dist

def shortest_path_time(N, M, grid):
    time = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'L':
                time = max(time, bfs(i, j, grid, N, M, directions))
    
    return time


def main():
    N, M = map(int, input().split())
    grid = [list(input().strip()) for _ in range(N)]

    print(shortest_path_time(N, M, grid))

if __name__ == '__main__':
    main()