# 영역 구하기 2583번
# https://www.acmicpc.net/problem/2583

# M: 세로길이, N: 가로 길이


######################## BFS ###############################
import sys
from collections import deque
def bfs(x,y,grid,visited,M,N):
    
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    area = 0
    
    # 상, 하, 좌, 우
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    while queue:
        cx, cy = queue.popleft()
        area += 1
        
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx,ny))
                
    return area

M, N, K = map(int,sys.stdin.readline().split())
grid = [[0]* N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int,sys.stdin.readline().split())
    
    for i in range(y1,y2):
        for j in range(x1,x2):
            grid[i][j] = 1
            
visited = [[False] * N for _ in range(M)]
areas = []

for i in range(M):
    for j in range(N):
        if grid[i][j] == 0 and not visited[i][j]:
            area = bfs(i,j,grid,visited,M,N)
            areas.append(area)
            
print(len(areas),' '.join(map(str,sorted(areas))),sep='\n')
######################## BFS ###############################


####################### DFS (stack) ########################
import sys
from collections import deque
def dfs_stack(x,y,grid,visited,M,N):
    
    stack = deque()
    stack.append((x,y))
    visited[x][y] = True
    area = 0
    
    # 상, 하, 좌, 우
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    while stack:
        cx, cy = stack.pop()
        area += 1
        
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                stack.append((nx,ny))
                
    return area

M, N, K = map(int,sys.stdin.readline().split())
grid = [[0]* N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int,sys.stdin.readline().split())
    
    for i in range(y1,y2):
        for j in range(x1,x2):
            grid[i][j] = 1
            
visited = [[False] * N for _ in range(M)]
areas = []

for i in range(M):
    for j in range(N):
        if grid[i][j] == 0 and not visited[i][j]:
            area = dfs_stack(i,j,grid,visited,M,N)
            areas.append(area)
            
print(len(areas),' '.join(map(str,sorted(areas))),sep='\n')
####################### DFS (stack) ########################


####################### DFS (recursive) ########################
import sys
sys.setrecursionlimit(10**6)
def dfs_recursive(x,y,grid,visited,M,N):
 
    visited[x][y] = True
    area = 1
    
    # 상, 하, 좌, 우
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == 0:
            area += dfs_recursive(nx,ny,grid,visited,M,N)
    
    return area

M, N, K = map(int,sys.stdin.readline().split())
grid = [[0]* N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int,sys.stdin.readline().split())
    
    for i in range(y1,y2):
        for j in range(x1,x2):
            grid[i][j] = 1
            
visited = [[False] * N for _ in range(M)]
areas = []

for i in range(M):
    for j in range(N):
        if grid[i][j] == 0 and not visited[i][j]:
            area = dfs_recursive(i,j,grid,visited,M,N)
            areas.append(area)
            
print(len(areas),' '.join(map(str,sorted(areas))),sep='\n')
####################### DFS (recursive) ########################