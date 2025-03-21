# 백준 2206. 벽 부수고 이동하기
# https://www.acmicpc.net/problem/2206
import sys
from collections import deque
def bfs(N, M, grid):

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]
    queue = deque([(0, 0, 1, 1)])
    visited[0][0][1] = True

    while queue:
        cur_x, cur_y, cur_d, cur_b = queue.popleft()

        if cur_x == N - 1 and cur_y == M - 1:
            return cur_d
        
        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy

            if 0 <= next_x < N and 0 <= next_y < M:

                if grid[next_x][next_y] == 0 and not visited[next_x][next_y][cur_b]:
                    visited[next_x][next_y][cur_b] = True
                    queue.append((next_x, next_y, cur_d + 1, cur_b))
                
                elif grid[next_x][next_y] == 1 and not visited[next_x][next_y][0] and cur_b == 1:
                    visited[next_x][next_y][0] = True
                    queue.append((next_x, next_y, cur_d + 1, 0))
    
    return -1

def main():
    N, M = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
    print(bfs(N, M, grid))

if __name__ == '__main__':
    main()