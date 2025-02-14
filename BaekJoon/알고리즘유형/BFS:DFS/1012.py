# 백준 1012. 유기농 배추
# https://www.acmicpc.net/problem/1012

################################# BFS 풀이 #################################
import sys
from collections import deque

def bfs(x, y, grid, visited, M, N):
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque()
    q.append((x, y))
    while q:
        cur_x, cur_y = q.popleft()
        for dx, dy in directions:
            next_x = cur_x + dx
            next_y = cur_y + dy
            
            if 0 <= next_x < M and 0 <= next_y < N:
                if grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    q.append((next_x, next_y))
    

T = int(sys.stdin.readline().strip())
    
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    grid = [[0] * N for _ in range(M)]
    visited = [[False] * N for _ in range(M)]
        
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        grid[x][y] = 1
        
    cnt = 0
    for i in range(M):
        for j in range(N):
                if grid[i][j] == 1 and not visited[i][j]:
                    bfs(i, j, grid, visited, M, N)
                    cnt += 1
    print(cnt)
################################# BFS 풀이 #################################

################################# DFS 풀이 #################################

import sys
sys.setrecursionlimit(10**6)
def dfs(x, y, grid, visited, M, N):
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        next_x = x + dx
        next_y = y + dy
            
        if 0 <= next_x < M and 0 <= next_y < N:
            if grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
               dfs(next_x, next_y, grid, visited, M, N)
    
T = int(sys.stdin.readline().strip())
    
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    grid = [[0] * N for _ in range(M)]
    visited = [[False] * N for _ in range(M)]
        
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        grid[x][y] = 1
        
    cnt = 0
    for i in range(M):
        for j in range(N):
                if grid[i][j] == 1 and not visited[i][j]:
                    dfs(i, j, grid, visited, M, N)
                    cnt += 1
    print(cnt)
################################# DFS 풀이 #################################