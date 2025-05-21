# 백준 2573. 빙산
# https://www.acmicpc.net/problem/2573
################################### 문제 이해 ###################################
# 빙산이 녹고 있다. 2차원 배열에 빙산의 높이 정보가 들어있다. 빙산 이외의 바다에 해당하는 칸에는 0
# 빙산의 높이는 바닷물에 많이 접해있는 부분에서 더 빨리 줄어든다.
# 배열에서 빙산의 각 부분에 해당되는 칸에 있는 높이는 일년마다 그 칸에 동서남북 네 방향으로
# 붙어있는 0이 저장된 칸의 개수만큼 줄어든다. 단, 각 칸에 저장된 높이는 0보다 더 줄어들지 않는다.
# 한 덩어리의 빙산이 주어질 때, 이 빙산이 두 덩어리 이상으로 분리되는 최초의 시간을 구해라.

################################### 문제 이해 ###################################
from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)

def melt(N, M, grid, directions):
    melt_list = []

    for x in range(1, N - 1):
        for y in range(1, M - 1):
            if grid[x][y] > 0:
                water_cnt = 0
                for dx, dy in directions:
                    next_x, next_y = x + dx, y + dy
                    if grid[next_x][next_y] == 0:
                        water_cnt += 1
                melt_list.append((x, y, water_cnt))
    
    for x, y, water in melt_list:
        grid[x][y] = max(0, grid[x][y] - water)
            
# def bfs(x, y, N, M, grid, directions, visited):
#     visited[x][y] = True
#     queue = deque([(x, y)])

#     while queue:
#         cur_x, cur_y = queue.popleft()

#         for dx, dy in directions:
#             next_x, next_y = cur_x + dx, cur_y + dy

#             if 0 <= next_x < N and 0 <= next_y < M:
#                 if grid[next_x][next_y] > 0 and not visited[next_x][next_y]:
#                     visited[next_x][next_y] = True
#                     queue.append((next_x, next_y))

def dfs(x, y, N, M, grid, directions, visited):
    visited[x][y] = True

    for dx, dy in directions:
        next_x, next_y = x + dx, y + dy

        if 0 <= next_x < N and 0 <= next_y < M:
            if grid[next_x][next_y] > 0 and not visited[next_x][next_y]:
                dfs(next_x, next_y, N, M, grid, directions, visited)

def count_bingsan(N, M, grid, directions):
    visited = [[False] * M for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(M):
            if grid[i][j] > 0 and not visited[i][j]:
                cnt += 1
                # bfs(i, j, N, M, grid, directions, visited)
                dfs(i, j, N, M, grid, directions, visited)
    
    return cnt

def sol(N, M, grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    year = 0

    while True:
        year += 1

        melt(N, M, grid, directions)
        cnt = count_bingsan(N, M, grid, directions)
        
        if cnt == 0:
            print(0)
            break
        elif cnt >= 2:
            print(year)
            break

def main():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    sol(N, M, grid)

if __name__ == '__main__':
    main()