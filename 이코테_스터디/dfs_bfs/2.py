# 미로 탈출
from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
def sol(n, m, grid):
    result = -1
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    
    if grid[0][0] != 1 and grid[n - 1][m - 1] != 1:
        return result
    
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    queue = deque()
    queue.append((0, 0, 1))
    while queue:
        cur_x, cur_y, cur_d = queue.popleft()
        
        if cur_x == n - 1 and cur_y == m - 1:
            result = cur_d
            break
        for dx, dy in directions:
            next_x = cur_x + dx
            next_y = cur_y + dy
            
            if 0 <= next_x < n and 0 <= next_y < m:
                if grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y, cur_d + 1))
    return result
print(sol(n=n, m=m, grid=grid))
