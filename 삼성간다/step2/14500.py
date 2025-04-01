# 백준 14500. 테트로미노
# https://www.acmicpc.net/problem/14500
def check_t_shape(x, y):
    global max_sum, t_shape, N, M

    for shape in t_shape:
        total = grid[x][y]
        valid = True

        for dx, dy in shape:
            next_x, next_y = x + dx, y + dy
            if 0 <= next_x < N and 0 <= next_y < M:
                total += grid[next_x][next_y]
            else:
                valid = False
                break
        
        if valid:
            max_sum = max(max_sum, total)

def dfs(x, y, depth, total):
    global max_sum, N, M, grid, visited
    directions = [(-1, 0), (1, 0), (0 ,-1), (0, 1)]

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
        
def solve_max_cnt(N, M, grid):
    global max_sum, visited
    max_sum = 0
    visited = [[False] * M for _ in range(N)]

    for x in range(N):
        for y in range(M):
            visited[x][y] = True
            dfs(x, y, 1, grid[x][y])
            visited[x][y] = False
            check_t_shape(x, y)
    
    return max_sum

def main():
    global N, M, grid, t_shape
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    t_shape = [
        [(0, -1), (-1, 0), (0, 1)],
        [(0, -1), (1, 0), (0, 1)],
        [(0, -1), (-1, 0), (1, 0)],
        [(0, 1), (-1, 0), (1, 0)]
    ]

    print(solve_max_cnt(N, M, grid))

if __name__ == '__main__':
    main()