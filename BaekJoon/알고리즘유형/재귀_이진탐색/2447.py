# 백준 2447. 별 찍기 -10
# https://www.acmicpc.net/problem/2447
import sys
N = int(sys.stdin.readline().strip())
grid = [[' ' for _ in range(N)] for _ in range(N)]

def sol(x, y, grid, size):
    
    # 1. base case
    if size == 3:
        grid[x][y] = '*'
        grid[x][y + 1] = '*'
        grid[x][y + 2] = '*'
        grid[x + 1][y] = '*'
        grid[x + 1][y + 1] = ' '
        grid[x + 1][y + 2] = '*'
        grid[x + 2][y] = '*'
        grid[x + 2][y + 1] = '*'
        grid[x + 2][y + 2] = '*'
        return
    new_size = size // 3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            sol(x + i * new_size, y + j * new_size, grid, new_size)

sol(0, 0, grid, N)
for row in grid:
    print(''.join(row))
