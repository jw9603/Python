# 백준 2583. 영역 구하기
# https://www.acmicpc.net/problem/2583
################################ BFS ################################
import sys
from collections import deque

def count_areas(M, N, grid):
    visited = [[False] * N for _ in range(M)]
    areas = []
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 0 and not visited[i][j]:
                areas.append(bfs(i, j, visited, grid, M, N))
    
    return len(areas), sorted(areas)

def bfs(x, y, visited, grid, M, N):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(x, y)])
    visited[x][y] = True
    size = 1
    while queue:
        cur_x, cur_y = queue.popleft()

        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy

            if 0 <= next_x < M and 0 <= next_y < N:
                if grid[next_x][next_y] == 0 and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y))
                    size += 1
    return size

def main():
    M, N, K = map(int, sys.stdin.readline().split())
    grid = [[0] * N for _ in range(M)]
    for _ in range(K):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

        for i in range(y1, y2):
            for j in range(x1, x2):
                grid[i][j] = 1
    
    cnt, areas = count_areas(M, N, grid)
    print(cnt)
    print(*areas)

if __name__ == '__main__':
    main()
################################ BFS ################################

################################ DFS ################################
import sys
sys.setrecursionlimit(10 ** 6)

def count_areas(M, N, grid):
    visited = [[False] * N for _ in range(M)]
    areas = []
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 0 and not visited[i][j]:
                areas.append(dfs(i, j, visited, grid, M, N))
    
    return len(areas), sorted(areas)

def dfs(x, y, visited, grid, M, N):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited[x][y] = True
    size = 1
    
    for dx, dy in directions:
        next_x, next_y = x + dx, y + dy

        if 0 <= next_x < M and 0 <= next_y < N:
            if grid[next_x][next_y] == 0 and not visited[next_x][next_y]:
                size += dfs(next_x, next_y, visited, grid, M, N)
    return size

def main():
    M, N, K = map(int, sys.stdin.readline().split())
    grid = [[0] * N for _ in range(M)]
    for _ in range(K):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

        for i in range(y1, y2):
            for j in range(x1, x2):
                grid[i][j] = 1
    
    cnt, areas = count_areas(M, N, grid)
    print(cnt)
    print(*areas)

if __name__ == '__main__':
    main()
################################ DFS ################################