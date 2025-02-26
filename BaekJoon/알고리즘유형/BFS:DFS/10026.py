# 백준 10026. 적록색약
# https://www.acmicpc.net/problem/10026
################################ DFS 풀이 #################################
import sys
sys.setrecursionlimit(10 ** 6)
def dfs(x, y, color, grid, visited, N):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited[x][y] = True
    
    for dx, dy in directions:
        next_x, next_y = x + dx, y + dy
        
        if 0 <= next_x < N and 0 <= next_y < N:
            if not visited[next_x][next_y] and grid[next_x][next_y] == color:
                dfs(next_x, next_y, color, grid, visited, N)

def count_regions(grid, N):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                dfs(i, j, grid[i][j], grid, visited, N)
                cnt += 1
    return cnt

def main():
    N = int(sys.stdin.readline().strip())
    grid = [list(sys.stdin.readline().strip()) for _ in range(N)]
    
    normal_cnt = count_regions(grid, N)
    
    blind_grid = [['G' if grid[i][j] == 'R' else grid[i][j] for j in range(N)] for i in range(N)]
    
    blind_cnt = count_regions(blind_grid, N)
    
    print(normal_cnt, blind_cnt)
main()
################################ DFS 풀이 #################################

################################ BFS 풀이 #################################
import sys
from collections import deque
def bfs(x, y, color, grid, visited, N):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited[x][y] = True
    queue = deque([(x, y)])
    
    while queue:
        cur_x, cur_y = queue.popleft()
        
        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy
                
            if 0 <= next_x < N and 0 <= next_y < N:
                if not visited[next_x][next_y] and grid[next_x][next_y] == color:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y))       

def count_regions(grid, N):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j, grid[i][j], grid, visited, N)
                cnt += 1
    return cnt

def main():
    N = int(sys.stdin.readline().strip())
    grid = [list(sys.stdin.readline().strip()) for _ in range(N)]
    
    normal_cnt = count_regions(grid, N)
    
    blind_grid = [['G' if grid[i][j] == 'R' else grid[i][j] for j in range(N)] for i in range(N)]
    
    blind_cnt = count_regions(blind_grid, N)
    
    print(normal_cnt, blind_cnt)
main()
################################ BFS 풀이 #################################