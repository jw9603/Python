# 백준 14500. 테트로미노
# https://www.acmicpc.net/problem/14500
import sys

N, M = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False] * M for _ in range(N)]

max_sum = 0

def dfs(x, y, depth, total):
    global max_sum
    
    if depth == 4:
        max_sum = max(max_sum, total)
        return
    for dx, dy in directions:
        next_x, next_y = x + dx, y + dy
        
        if 0 <= next_x < N and 0 <= next_y < M:
            if not visited[next_x][next_y]:
                visited[next_x][next_y] = True
                dfs(next_x, next_y, depth + 1, total + grid[next_x][next_y])
                visited[next_x][next_y] = False
                
def check_t_shape(x, y):
    """ 'ㅗ', 'ㅓ', 'ㅏ', 'ㅜ'  모양 처리"""
    global max_sum
    
    for shape in [
        [(0, -1), (0, 1), (-1, 0)],
        [(0, -1), (0, 1), (1, 0)],
        [(0, 1), (-1, 0), (1, 0)],
        [(0, -1), (-1, 0), (1, 0)]
    ]:
        total = grid[x][y]
        valid = True
        
        for dx, dy in shape:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M:
                total += grid[nx][ny]
            else:
                valid = False
                break
        if valid:
            max_sum = max(total, max_sum)
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1 ,grid[i][j])
        visited[i][j] = False
        check_t_shape(i, j)
print(max_sum)
        