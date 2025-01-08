# 음료수 얼려 먹기

############################################## 내 풀이 1. BFS 풀이 ##############################################
import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
result = 0
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상 하 좌 우
def bfs(x, y):
    visited[x][y] = True
    q = deque()
    q.append((x, y))
    while q:
        cur_x, cur_y = q.popleft()
        
        for dx, dy in directions:
            next_x = cur_x + dx
            next_y = cur_y + dy
            
            if 0 <= next_x < n and 0 <= next_y < m:
                if grid[next_x][next_y] == 0 and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    q.append((next_x, next_y))
    

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0 and not visited[i][j]:
            bfs(i, j)
            result += 1
print(result)
############################################## 내 풀이 1. BFS 풀이 ##############################################

############################################## 내 풀이 2. DFS 풀이 ##############################################
import sys
n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
result = 0
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상 하 좌 우

def dfs(x, y):
    visited[x][y] = True
    
    for dx, dy in directions:
        next_x = x + dx
        next_y = y + dy
        
        if 0 <= next_x < n and 0 <= next_y < m:
            if grid[next_x][next_y] == 0 and not visited[next_x][next_y]:
                dfs(next_x, next_y)

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0 and not visited[i][j]:
            dfs(i, j)
            result += 1
print(result)
############################################## 내 풀이 2. DFS 풀이 ##############################################