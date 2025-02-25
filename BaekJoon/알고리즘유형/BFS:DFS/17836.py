# 백준 17836. 공주님을 구해라!
# https://www.acmicpc.net/problem/17836
import sys
from collections import deque
def bfs(N, M, grid, T):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * M for _ in range(N)]
    queue = deque([(0, 0, 0)])
    
    gram_time = float('inf')
    
    while queue:
        cur_x, cur_y, cur_t = queue.popleft()
        
        if cur_t > T:
            break
        
        if cur_x == N - 1 and cur_y == M - 1:
            return min(gram_time, cur_t)
        
        if grid[cur_x][cur_y] == 2:
            gram_time = cur_t + (N - 1 - cur_x) + (M - 1 - cur_y)
            continue
        
        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy
            
            if 0 <= next_x < N and 0 <= next_y < M and not visited[next_x][next_y]:
                if grid[next_x][next_y] == 0 or grid[next_x][next_y] == 2:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y, cur_t + 1))
    return gram_time

def main():
    N, M, T = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    
    min_time = bfs(N, M, grid, T)
    
    if min_time <= T:
        print(min_time)
    else:
        print("Fail")
main()