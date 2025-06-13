# 백준 1743. 음식물 피하기
# https://www.acmicpc.net/problem/1743
############################### 문제 이해 ###############################
# 8층: 3끼의 식사를 해결하는 공간, 음식물이 통로 중간 중간에 떨어져 있다.
# 이러한 음식물들은 근처에 있는 것끼리 뭉치게 돼서 큰 음식물 쓰레기가 된다.

# 선생님은 음식물 중에 제일 큰 음식물 만은 피해 가려고 한다.
# 즉, 음식물 중 가장 큰 음식물의 크기를 출력하라.

# 입력: N과 M, K이 주어진다.
# 그 다음 K개의 줄에 음식물이 떨어진 좌표 (r, c)가 주어진다.

# 알고리즘
# 음식물들은 근처에 있는것들끼리 뭉쳐서 크게 된다고 했다. 즉, 인접한 것들끼리 뭉치는것
# 따라서 쉽게 생각해서 가장 큰 섬의 개수를 세는 것
# BFS, DFS 모두 사용 가능
############################### 문제 이해 ###############################
# BFS
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

def solve_max_trash(N, M, grid, visited):
    max_size = 0

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1 and not visited[i][j]:
                max_size = max(max_size, bfs(i, j, N, M, grid, visited))

    return max_size

def main():
    N, M, K = map(int, input().split())
    grid = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        r, c = map(int, input().split()) 
        grid[r - 1][c - 1] = 1

    print(solve_max_trash(N, M, grid, visited))   

if __name__ == '__main__':
    main()

# DFS
import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x, y, N, M, grid, visited):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited[x][y] = True
    size = 1
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < N and 0 <= ny < M:
            if grid[nx][ny] == 1 and not visited[nx][ny]:
                size += dfs(nx, ny, N, M, grid, visited)
    
    return size

def solve_max_trash(N, M, grid, visited):
    max_size = 0

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1 and not visited[i][j]:
                max_size = max(max_size, dfs(i, j, N, M, grid, visited))
    
    return max_size

def main():
    N, M, K = map(int, input().split())
    grid = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        r, c = map(int, input().split()) 
        grid[r - 1][c - 1] = 1

    print(solve_max_trash(N, M, grid, visited))   

if __name__ == '__main__':
    main()