# 백준 11123번 - 양 한마리... 양 두마리...
# https://www.acmicpc.net/problem/11123

# 문제 이해
# 양: #, .: 풀

import sys
from collections import deque


#################### dfs (stack) ##################################
def dfs(grid,visited,x,y,H,W):
    
    # 상, 하, 좌, 우
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    stack = deque([(x,y)])
    visited[x][y] = True
    
    while stack:
        cx, cy = stack.pop()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and grid[nx][ny] == '#':
                visited[nx][ny] = True
                stack.append((nx,ny))
                
                
def count_sheep_groups(grid,H,W):
    
    visited = [[False]*W for _ in range(H)]
    cnt = 0
    
    for h in range(H):
        for w in range(W):
            if grid[h][w] == '#' and not visited[h][w]:
                dfs(grid,visited,h,w,H,W)
                cnt += 1
    
    return cnt 

T = int(sys.stdin.readline().strip())

for _ in range(T):
    H, W = map(int,sys.stdin.readline().split())
    grid = [sys.stdin.readline().strip() for _ in range(H)]
    
    result = count_sheep_groups(grid,H,W)
#################### dfs (stack) ##################################


#################### dfs (recursive) ##################################
import sys
sys.setrecursionlimit(10**6)

def dfs_recursive(grid, visited, x, y, H, W):
    # 상, 하, 좌, 우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited[x][y] = True
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and grid[nx][ny] == '#':
            dfs_recursive(grid, visited, nx, ny, H, W)

def count_sheep_groups_dfs_recursive(grid, H, W):
    visited = [[False] * W for _ in range(H)]
    cnt = 0
    
    for h in range(H):
        for w in range(W):
            if grid[h][w] == '#' and not visited[h][w]:
                dfs_recursive(grid, visited, h, w, H, W)
                cnt += 1
    
    return cnt 

T = int(sys.stdin.readline().strip())

for _ in range(T):
    H, W = map(int, sys.stdin.readline().split())
    grid = [sys.stdin.readline().strip() for _ in range(H)]
    
    result = count_sheep_groups_dfs_recursive(grid, H, W)
    print(result)

#################### dfs (recursive) ##################################


############################# BFS #################################
import sys
from collections import deque  # 이 줄이 필요합니다.

def bfs(grid, visited, x, y, H, W):
    # 상, 하, 좌, 우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(x, y)])
    visited[x][y] = True
    
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and grid[nx][ny] == '#':
                visited[nx][ny] = True
                queue.append((nx, ny))

def count_sheep_groups(grid, H, W):
    visited = [[False] * W for _ in range(H)]
    cnt = 0
    
    for h in range(H):
        for w in range(W):
            if grid[h][w] == '#' and not visited[h][w]:
                bfs(grid, visited, h, w, H, W)
                cnt += 1
    
    return cnt 

T = int(sys.stdin.readline().strip())

for _ in range(T):
    H, W = map(int, sys.stdin.readline().split())
    grid = [sys.stdin.readline().strip() for _ in range(H)]
    
    result = count_sheep_groups(grid, H, W)
    print(result)

############################# BFS #################################





    

    