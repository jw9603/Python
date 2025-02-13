# 백준 2178. 미로 탐색
# https://www.acmicpc.net/problem/2178
import sys
from collections import deque
def bfs(N, M, grid):
    visited = [[False] * M for _ in range(N)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque()
    q.append((0, 0, 1))
    result = 0
    while q:
        cur_x, cur_y, cur_d = q.popleft()
        if cur_x == N - 1 and cur_y == M - 1:
            result = cur_d
            return result
        for dx, dy in directions:
            next_x = cur_x + dx
            next_y = cur_y + dy
            
            if 0 <= next_x < N and 0 <= next_y < M:
                if grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    q.append((next_x, next_y, cur_d + 1))
    

def main():
    N, M = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
    
    print(bfs(N=N, M=M, grid=grid))
main()
        