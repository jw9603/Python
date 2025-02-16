# 백준 7576. 토마토
# https://www.acmicpc.net/problem/7576
import sys
from collections import deque
def bfs(m, n, grid):
    directons = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    result = 0
    unripe_cnt = 0
    queue = deque()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                queue.append((i, j, 0))
            elif grid[i][j] == 0:
                unripe_cnt += 1
    
    while queue:
        cur_x, cur_y, days = queue.popleft()
        result = max(result, days)
        for dx, dy in directons:
            next_x, next_y = cur_x + dx, cur_y + dy
            
            if 0 <= next_x < n and 0 <= next_y < m:
                if grid[next_x][next_y] == 0:
                    grid[next_x][next_y] = 1
                    unripe_cnt -= 1
                    queue.append((next_x, next_y, days + 1))
    return result if not unripe_cnt else -1
    

def main():
    M, N = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    print(bfs(M, N, grid))
main()