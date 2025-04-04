# 백준 16234. 인구 인동
# https://www.acmicpc.net/problem/16234
from collections import deque
def bfs(x, y, grid, visited, N, L, R):
    queue = deque([(x, y)])
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    union = [(x, y)]
    total_population = grid[x][y]

    while queue:
        cur_x, cur_y = queue.popleft()

        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy

            if 0 <= next_x < N and 0 <= next_y < N and not visited[next_x][next_y]:
                if L <= abs(grid[cur_x][cur_y] - grid[next_x][next_y]) <= R:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y))
                    union.append((next_x, next_y))
                    total_population += grid[next_x][next_y]
    
    if len(union) > 1:
        new_population = total_population // len(union)
        for ux, uy in union:
            grid[ux][uy] = new_population
        return True
    return False

def sol(N, L, R, grid):
    days = 0

    while True:
        visited = [[False] * N for _ in range(N)]
        move = False

        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    if bfs(i, j, grid, visited, N, L, R):
                        move = True
        
        if not move:
            break
        days += 1
    
    return days

def main():
    N, L, R = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    print(sol(N, L, R, grid))

if __name__ == '__main__':
    main()