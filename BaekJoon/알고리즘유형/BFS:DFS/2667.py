# 백준 2667. 단지번호붙이기
# https://www.acmicpc.net/problem/2667
import sys
n = int(sys.stdin.readline().strip())
grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
result = 0
home_cnt = []
def dfs(x, y):
    visited[x][y] = True
    count = 1
    
    for dx, dy in directions:
        next_x, next_y = x + dx, y + dy
        if 0 <= next_x < n and 0 <= next_y < n:
            if grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
                count += dfs(next_x, next_y)
    
    return count
                
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            home_cnt.append(dfs(i, j))
            result += 1
print(result, '\n'.join(map(str, sorted(home_cnt))),sep='\n')
            