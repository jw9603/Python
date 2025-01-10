# 백준 1992. 쿼드트리
# https://www.acmicpc.net/problem/1992
import sys
N = int(sys.stdin.readline().strip())
matrix = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
def sol(x, y, size):
    first_val = matrix[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if matrix[i][j] != first_val:
                new_size = size // 2
                top_left = sol(x, y, new_size)
                top_right = sol(x, y + new_size, new_size)
                bottom_left = sol(x + new_size, y, new_size)
                bottom_right = sol(x + new_size, y + new_size, new_size)
                
                return f"({top_left}{top_right}{bottom_left}{bottom_right})"
    return first_val

print(sol(0, 0, N))