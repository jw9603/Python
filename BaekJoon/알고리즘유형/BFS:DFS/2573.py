# 백준 2573. 빙산
# https://www.acmicpc.net/problem/2573
############################## BFS ##############################
# import sys
# from collections import deque

# def melt(N, M, grid, directions):
#     melt_list = []
    
#     for x in range(1, N - 1):
#         for y in range(1, M - 1):
#             if grid[x][y] > 0:
#                 water_cnt = 0
#                 for dx, dy in directions:
#                     next_x, next_y = x + dx, y + dy
#                     if grid[next_x][next_y] == 0:
#                         water_cnt += 1
#                 melt_list.append((x, y, water_cnt))
#     for x, y, water in melt_list:
#         grid[x][y] = max(0, grid[x][y] - water)
            

# def count_binsang(N, M, grid, directions):
#     visited = [[False] * M for _ in range(N)]
#     cnt = 0
    
#     for x in range(1, N - 1):
#         for y in range(1, M - 1):
#             if grid[x][y] > 0 and not visited[x][y]:
#                 cnt += 1
#                 if cnt > 1:
#                     return cnt
#                 bfs(x, y, visited, N, M, grid, directions)
#     return cnt

# def bfs(x, y, visited, N, M, grid, directions):
#     queue = deque([(x, y)])
#     visited[x][y] = True
    
#     while queue:
#         cur_x, cur_y = queue.popleft()
#         for dx, dy in directions:
#             next_x, next_y =  cur_x + dx, cur_y + dy
            
#             if 0 <= next_x < N and 0 <= next_y < M:
#                 if grid[next_x][next_y] > 0 and not visited[next_x][next_y]:
#                     visited[next_x][next_y] = True
#                     queue.append((next_x, next_y))

# def main():
#     N, M = map(int, sys.stdin.readline().split())
#     grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#     years = 0
    
#     while True:
#         melt(N=N, M=M, grid=grid, directions=directions)
#         years += 1
        
#         cnt = count_binsang(N=N, M=M, grid=grid, directions=directions)
        
#         if cnt == 0:
#             print(0)
#             break
#         elif cnt >= 2:
#             print(years)
#             break
# main() 
############################## BFS ##############################

############################## DFS ##############################
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
            

def count_binsang(N, M, grid, directions):
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    
    for x in range(1, N - 1):
        for y in range(1, M - 1):
            if grid[x][y] > 0 and not visited[x][y]:
                cnt += 1
                if cnt > 1:
                    return cnt
                dfs(x, y, visited, N, M, grid, directions)
    return cnt

def dfs(x, y, visited, N, M, grid, directions):

    visited[x][y] = True

    for dx, dy in directions:
        next_x, next_y =  x + dx, y + dy
            
        if 0 <= next_x < N and 0 <= next_y < M:
            if grid[next_x][next_y] > 0 and not visited[next_x][next_y]:
                dfs(next_x, next_y, visited, N, M, grid, directions)

def main():
    N, M = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    years = 0
    
    while True:
        melt(N=N, M=M, grid=grid, directions=directions)
        years += 1
        
        cnt = count_binsang(N=N, M=M, grid=grid, directions=directions)
        
        if cnt == 0:
            print(0)
            break
        elif cnt >= 2:
            print(years)
            break
main() 
############################## DFS ##############################