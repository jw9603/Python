# 백준 2589. 보물섬
# https://www.acmicpc.net/problem/2589
import sys
from collections import deque
def bfs(x, y, grid, N, M, directions):
    queue = deque([(x, y, 0)])
    visited = [[False] * M for _ in range(N)]
    visited[x][y] = True
    max_distance = 0
    
    while queue:
        cur_x, cur_y, cur_d = queue.popleft()
        max_distance = max(max_distance, cur_d)
        
        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy
            if 0 <= next_x < N and 0 <= next_y < M:
                if grid[next_x][next_y] == 'L' and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y, cur_d + 1))
    return max_distance

def main():
    N, M = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().strip()) for _ in range(N)]
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    max_time = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'L':
                max_time = max(max_time, bfs(i, j, grid, N, M, directions))
    print(max_time)
main()