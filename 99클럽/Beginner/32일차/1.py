# 6080
# https://www.acmicpc.net/problem/6080

# R행과 C열


################## DFS (recursive) ##############################
# import sys

# sys.setrecursionlimit(10**6)  # 재귀 깊이를 충분히 큰 값으로 설정

# def count_bad_grass(grid,R,C):
    
#     def dfs(r,c): # r: 행, c: 열
#         if r < 0 or c < 0 or r >= R or c >= C or grid[r][c] == 0:
#             return
        
#         grid[r][c] = 0
        
#         dfs(r-1,c)    # 상
#         dfs(r+1,c)    # 하
#         dfs(r,c-1)    # 좌
#         dfs(r,c+1)    # 우
#         dfs(r-1,c-1)  
#         dfs(r+1,c+1)
#         dfs(r+1,c-1)
#         dfs(r-1,c+1)
    
#     cnt = 0
#     for r in range(R):
#         for c in range(C):
#             if grid[r][c] > 0:
#                 dfs(r,c)
#                 cnt += 1
#     return cnt


# R, C = map(int,sys.stdin.readline().split())

# grid = []

# for _ in range(R):
#     grid.append(list(map(int,sys.stdin.readline().split())))
    

# print(count_bad_grass(grid,R,C))
################## DFS (recursive) ##############################

######################### DFS (stack) ###########################
import sys
from collections import deque
def count_bad_grass(grid,R,C):
    
    def dfs_stack(r,c):
        stack = deque([(r,c)])
        while stack:
            r,c = stack.pop()
            if r < 0 or c < 0 or r >= R or c >= C or grid[r][c] == 0:
                continue
            
            grid[r][c] = 0
            
            stack.append((r-1,c))
            stack.append((r+1,c))
            stack.append((r,c-1))
            stack.append((r,c+1))
            stack.append((r+1,c+1))
            stack.append((r-1,c-1))
            stack.append((r+1,c-1))
            stack.append((r-1,c+1))
            
    cnt = 0
    
    for r in range(R):
        for c in range(C):
            if grid[r][c] > 0:
                dfs_stack(r,c)
                cnt += 1
    return cnt

R, C = map(int,sys.stdin.readline().split())

grid = []

for _ in range(R):
    grid.append(list(map(int,sys.stdin.readline().split())))
    

print(count_bad_grass(grid,R,C))
######################### DFS (stack) ###########################


######################### BFS ###########################
import sys
from collections import deque
def count_bad_grass(grid,R,C):
    
    def bfs_queue(r,c):
        queue = deque([(r,c)])
        while queue:
            r,c = queue.popleft()
            if r < 0 or c < 0 or r >= R or c >= C or grid[r][c] == 0:
                continue
            
            grid[r][c] = 0
            
            queue.append((r-1,c))
            queue.append((r+1,c))
            queue.append((r,c-1))
            queue.append((r,c+1))
            queue.append((r+1,c+1))
            queue.append((r-1,c-1))
            queue.append((r+1,c-1))
            queue.append((r-1,c+1))
            
    cnt = 0
    
    for r in range(R):
        for c in range(C):
            if grid[r][c] > 0:
                bfs_queue(r,c)
                cnt += 1
    return cnt

R, C = map(int,sys.stdin.readline().split())

grid = []

for _ in range(R):
    grid.append(list(map(int,sys.stdin.readline().split())))
    

print(count_bad_grass(grid,R,C))
######################### BFS ###########################