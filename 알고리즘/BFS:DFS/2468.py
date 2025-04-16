# 백준 2468. 안전 영역
# https://www.acmicpc.net/problem/2468
############################# 문제 이해 #############################
# 일정한 높이 이하의 모든 지점은 물에 잠긴다.
# 물에 잠기지 않는 안전한 영역 -> 물에 잠기지 않는 지점들이 위, 아래, 오른쪽, 왼쪽
# 으로 인접해 있다. 이것이 안전한 영역이 되는것
# 안전한 영역의 최대 개수를 계산하는 프로그램을 작성해라.
############################# 문제 이해 #############################
############################# BFS #############################
from collections import deque
def bfs(N, x, y, grid, water_level, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        cur_x, cur_y = queue.popleft()

        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy

            if 0 <= next_x < N and 0 <= next_y < N:
                if not visited[next_x][next_y] and grid[next_x][next_y] > water_level:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y))

def count_safe_areas(N, grid, water_level):
    cnt = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and grid[i][j] > water_level:
                bfs(N, i, j, grid, water_level, visited)
                cnt += 1
    
    return cnt

def sol(N, grid):
    result = 0
    max_height = max(map(max, grid))
    min_height = min(map(min, grid))

    for water_level in range(min_height - 1, max_height + 1):
        cnt = count_safe_areas(N, grid, water_level)
        result = max(result, cnt)
    
    return result

def main():
    N = int(input().strip())
    grid = [list(map(int, input().split())) for _ in range(N)]

    print(sol(N, grid))

if __name__ == '__main__':
    main()
############################# BFS #############################

############################# DFS #############################
import sys
sys.setrecursionlimit(10 ** 6)
def dfs(N, x, y, grid, water_level, visited):
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        next_x, next_y = x + dx, y + dy

        if 0 <= next_x < N and 0 <= next_y < N:
            if not visited[next_x][next_y] and grid[next_x][next_y] > water_level:
                dfs(N, next_x, next_y, grid, water_level, visited)

def count_safe_areas(N, grid, water_level):
    cnt = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and grid[i][j] > water_level:
                dfs(N, i, j, grid, water_level, visited)
                cnt += 1
    
    return cnt

def sol(N, grid):
    result = 0
    max_height = max(map(max, grid))
    min_height = min(map(min, grid))

    for water_level in range(min_height - 1, max_height + 1):
        cnt = count_safe_areas(N, grid, water_level)
        result = max(result, cnt)
    
    return result

def main():
    N = int(input().strip())
    grid = [list(map(int, input().split())) for _ in range(N)]

    print(sol(N, grid))

if __name__ == '__main__':
    main()
############################# DFS #############################