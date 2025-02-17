# 백준 4963. 섬의 개수
# https://www.acmicpc.net/problem/4963
################################# BFS 풀이 ##################################
import sys
from collections import deque

def bfs(x, y, w, h, grid, visited):
    queue = deque([(x, y)])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    visited[y][x] = True
    
    while queue:
        cur_x, cur_y = queue.popleft()
        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy
            if 0 <= next_x < w and 0 <= next_y < h:
                if grid[next_y][next_x] == 1 and not visited[next_y][next_x]:
                    visited[next_y][next_x] = True
                    queue.append((next_x, next_y))
                

def count_islands(w, h, grid, visited):
    cnt = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and not visited[i][j]:
                bfs(j, i, w, h, grid, visited)
                cnt += 1
    return cnt
                

def main():
    while True:
        w, h = map(int, sys.stdin.readline().split())
        if w == 0 and h == 0:
            break
        visited = [[False] * w for _ in range(h)]
        grid = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
        print(count_islands(w=w, h=h, grid=grid, visited=visited))
main()      
################################# BFS 풀이 ##################################

################################# DFS 풀이 ##################################
import sys
sys.setrecursionlimit(10**6)
def dfs(x, y, w, h, grid, visited):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    visited[y][x] = True
    for dx, dy in directions:
        next_x = x + dx
        next_y = y + dy
        if 0 <= next_x < w and 0 <= next_y < h:
            if grid[next_y][next_x] == 1 and not visited[next_y][next_x]:
                dfs(next_x, next_y, w, h, grid, visited)

def count_islands(w, h, grid, visited):
    cnt = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and not visited[i][j]:
                dfs(j, i, w, h, grid, visited)
                cnt += 1
    return cnt

def main():
    while True:
        w, h = map(int, sys.stdin.readline().split())
        if w == 0 and h == 0:
            break
        visited = [[False] * w for _ in range(h)]
        grid = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
        print(count_islands(w=w, h=h, grid=grid, visited=visited))
main()    
################################# DFS 풀이 ##################################