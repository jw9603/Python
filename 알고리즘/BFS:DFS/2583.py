# 백준 2583. 영역 구하기
# https://www.acmicpc.net/problem/2583
############################## 문제 이해 ##############################
# M * N 크기의 모눈종이가 있다.
# K개의 직사각형을 그릴 때, 이들 K개의 직사각형의 내부를 제외한 나머지 부분이 몇 개의 분리된
# 영역으로 나누어진다.

# K개의 직사각형의 좌표가 주어질 때, K개의 직사각형 내부를 제외한 나머지 부분이
# 몇 개의 분리된 영역으로 나누어지는지, 그리고 분리된 각 영역의 넓이가 얼마인지를 구해라
############################## 문제 이해 ##############################
############################# BFS #############################
from collections import deque
def bfs(M, N, i, j, grid, visited):
    visited[i][j] = True
    queue = deque([(i, j)])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    sizes = 1

    while queue:
        cur_x, cur_y = queue.popleft()

        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy

            if 0 <= next_x < M and 0 <= next_y < N:
                if grid[next_x][next_y] == 0 and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    sizes += 1
                    queue.append((next_x, next_y))
    
    return sizes

def count_areas(M, N, grid):
    cnt = 0
    areas = []
    visited =[[False] * N for _ in range(M)]

    for i in range(M):
        for j in range(N):
            if grid[i][j] == 0 and not visited[i][j]:
                cnt += 1
                areas.append(bfs(M, N, i, j, grid, visited))
    
    return cnt, sorted(areas)

def main():
    M, N, K = map(int, input().split())
    grid = [[0] * N for _ in range(M)]
    for _ in range(K):
        x1, y1, x2, y2 = map(int, input().split())

        for i in range(y1, y2):
            for j in range(x1, x2):
                grid[i][j] = 1
    
    area_cnt, areas = count_areas(M, N, grid)
    print(area_cnt)
    print(*areas)

if __name__ == '__main__':
    main()
############################# BFS #############################
############################# DFS #############################
import sys
sys.setrecursionlimit(10 ** 6)

def dfs(M, N, x, y, grid, visited):
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    sizes = 1

    for dx, dy in directions:
        next_x, next_y = x + dx, y + dy

        if 0 <= next_x < M and 0 <= next_y < N:
            if grid[next_x][next_y] == 0 and not visited[next_x][next_y]:
                sizes += dfs(M, N, next_x, next_y, grid, visited)
    
    return sizes

def count_areas(M, N, grid):
    cnt = 0
    areas = []
    visited =[[False] * N for _ in range(M)]

    for i in range(M):
        for j in range(N):
            if grid[i][j] == 0 and not visited[i][j]:
                cnt += 1
                areas.append(dfs(M, N, i, j, grid, visited))
    
    return cnt, sorted(areas)

def main():
    M, N, K = map(int, input().split())
    grid = [[0] * N for _ in range(M)]
    for _ in range(K):
        x1, y1, x2, y2 = map(int, input().split())

        for i in range(y1, y2):
            for j in range(x1, x2):
                grid[i][j] = 1
    
    area_cnt, areas = count_areas(M, N, grid)
    print(area_cnt)
    print(*areas)

if __name__ == '__main__':
    main()
############################# DFS #############################