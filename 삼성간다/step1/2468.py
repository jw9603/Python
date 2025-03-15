# 백준 2468. 안전 영역
# https://www.acmicpc.net/problem/2468
################################### BFS 풀이 #########################################
import sys
from collections import deque
def dfs(x, y, visited, grid, N, water_level):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited[x][y] = True

    for dx, dy in directions:
        next_x, next_y = x + dx, y + dy
        if 0 <= next_x < N and 0 <= next_y < N:
            if not visited[next_x][next_y] and grid[next_x][next_y] > water_level:
                dfs(next_x, next_y, visited, grid, N, water_level)
        
def bfs(x, y, visited, grid, N, water_level):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        cur_x, cur_y = queue.popleft()
        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy
            if 0 <= next_x < N and 0 <= next_y < N:
                if not visited[next_x][next_y] and grid[next_x][next_y] > water_level:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y))

def count_safe_areas(N, grid, water_level):
    visited = [[False] * N for _ in range(N)]
    safe_area_cnt = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and grid[i][j] > water_level:
                safe_area_cnt += 1
                bfs(i, j, visited, grid, N, water_level)
    return safe_area_cnt

def main():
    N = int(sys.stdin.readline().strip())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    min_height = min(map(min, grid))
    max_height = max(map(max, grid))

    max_safe_areas = 1

    for water_level in range(min_height - 1, max_height + 1):
        safe_areas = count_safe_areas(N, grid, water_level)
        max_safe_areas = max(safe_areas, max_safe_areas)
    
    print(max_safe_areas)

if __name__ == '__main__':
    main()
################################### BFS 풀이 #########################################

################################### DFS 풀이 #########################################
import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
def dfs(x, y, visited, grid, N, water_level):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited[x][y] = True

    for dx, dy in directions:
        next_x, next_y = x + dx, y + dy
        if 0 <= next_x < N and 0 <= next_y < N:
            if not visited[next_x][next_y] and grid[next_x][next_y] > water_level:
                dfs(next_x, next_y, visited, grid, N, water_level)
        
def count_safe_areas(N, grid, water_level):
    visited = [[False] * N for _ in range(N)]
    safe_area_cnt = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and grid[i][j] > water_level:
                safe_area_cnt += 1
                dfs(i, j, visited, grid, N, water_level)
    return safe_area_cnt

def main():
    N = int(sys.stdin.readline().strip())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    min_height = min(map(min, grid))
    max_height = max(map(max, grid))

    max_safe_areas = 1

    for water_level in range(min_height - 1, max_height + 1):
        safe_areas = count_safe_areas(N, grid, water_level)
        max_safe_areas = max(safe_areas, max_safe_areas)
    
    print(max_safe_areas)

if __name__ == '__main__':
    main()
################################### DFS 풀이 #########################################