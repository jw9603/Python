# 백준 2448. 별 찍기 - 11
# https://www.acmicpc.net/problem/2448
import sys
N = int(sys.stdin.readline().strip())
grid = [[' ' for _ in range(2 * N - 1)] for _ in range(N)]

def sol(x, y, grid, size):
    if size == 3:
        grid[x][y] = '*'
        grid[x+1][y-1] = '*'
        grid[x+1][y+1] = '*'
        grid[x+1][y] = ' '
        grid[x+2][y-2] = '*'
        grid[x+2][y-1] = '*'
        grid[x+2][y] = '*'
        grid[x+2][y+1] = '*'
        grid[x+2][y+2] = '*'
        return
    new_size = size // 2
    sol(x, y, grid, new_size)
    sol(x + new_size, y - new_size, grid, new_size)
    sol(x + new_size, y + new_size, grid, new_size)

sol(0, N - 1, grid, N)
for row in grid:
    print(''.join(row))
