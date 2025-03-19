# 백준 2665. 미로만들기
# https://www.acmicpc.net/problem/2665
import sys
from collections import deque
def bfs(n, grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    queue = deque([(0, 0, 0)]) # 변경 횟수, x, y
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = 0

    while queue:
        cur_cnt, cur_x, cur_y = queue.popleft()

        if cur_x == n - 1 and cur_y == n - 1:
            return cur_cnt
        
        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy
            
            if 0 <= next_x < n and 0 <= next_y < n:
                if not visited[next_x][next_y]:
                    visited[next_x][next_y] = True

                    if grid[next_x][next_y] == 0:
                        queue.append((cur_cnt + 1, next_x, next_y))
                    else:
                        queue.appendleft((cur_cnt, next_x, next_y))

def main():
    n = int(sys.stdin.readline().strip())
    grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
    print(bfs(n, grid))

if __name__ == '__main__':
    main()