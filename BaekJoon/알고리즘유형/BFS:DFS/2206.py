# 백준 2206. 벽 부수고 이동하기
# https://www.acmicpc.net/problem/2206
from collections import deque
import sys
def bfs(N, M, grid):
    
    # visited[x][y][0]: 벽을 부수고 방문하는 경우, visited[x][y][1]: 벽을 부수지 않고 방문하는 경우
    visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    queue = deque([(0, 0, 1, 1)])
    visited[0][0][1] = True
    
    while queue:
        cur_x, cur_y, cur_d, break_chance = queue.popleft()
        
        if cur_x == N - 1 and cur_y == M - 1:
            return cur_d
        
        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy
            
            if 0 <= next_x < N and 0 <= next_y < M:
                if grid[next_x][next_y] == 0 and not visited[next_x][next_y][break_chance]:
                    visited[next_x][next_y][break_chance] = True
                    queue.append((next_x, next_y, cur_d + 1, break_chance))
                
                elif grid[next_x][next_y] == 1 and break_chance == 1 and not visited[next_x][next_y][0]:
                    visited[next_x][next_y][0] = True
                    queue.append((next_x, next_y, cur_d + 1, 0))
    return -1

def main():
    N, M = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
    print(bfs(N=N, M=M, grid=grid))
main()
    