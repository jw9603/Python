# 백준 1743. 음식물 피하기
# https://www.acmicpc.net/problem/1743
################################## BFS ##################################
import sys
from collections import deque
def bfs(x, y, N, M, grid, visited):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(x, y)])
    visited[x][y] = True
    size = 1

    while queue:
        cur_x, cur_y = queue.popleft()

        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy

            if 0 <= next_x < N and 0 <= next_y < M:
                if grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y))
                    size += 1
    return size

def print_max_size(N, M, grid, visited):
    max_size = 0

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1 and not visited[i][j]:
                max_size = max(max_size, bfs(i, j, N, M, grid, visited))
    
    return max_size

def main():
    N, M, K = map(int, sys.stdin.readline().split())
    grid = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        r, c = map(int, sys.stdin.readline().split())
        grid[r - 1][c - 1] = 1

    print(print_max_size(N, M, grid, visited))

if __name__ == '__main__':
    main()
################################## BFS ##################################

################################## DFS ##################################
import sys
sys.setrecursionlimit(10 ** 6)
def dfs(x, y, N, M, grid, visited):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited[x][y] = True
    size = 1

    for dx, dy in directions:
        next_x, next_y = x + dx, y + dy

        if 0 <= next_x < N and 0 <= next_y < M:
            if grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
                size += dfs(next_x, next_y, N, M, grid, visited)
    return size

def print_max_size(N, M, grid, visited):
    max_size = 0

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1 and not visited[i][j]:
                max_size = max(max_size, dfs(i, j, N, M, grid, visited))
    
    return max_size

def main():
    N, M, K = map(int, sys.stdin.readline().split())
    grid = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        r, c = map(int, sys.stdin.readline().split())
        grid[r - 1][c - 1] = 1

    print(print_max_size(N, M, grid, visited))

if __name__ == '__main__':
    main()
################################## DFS ##################################