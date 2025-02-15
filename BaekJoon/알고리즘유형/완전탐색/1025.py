# 백준 1025. 제곱수 찾기
# https://www.acmicpc.net/problem/1025
import sys
import math

N, M = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().strip()) for _ in range(N)]
def is_perfect_square(num):
    if num < 0:
        return False
    return int(math.sqrt(num)) ** 2 == num

def sol(N, M, grid):
    max_square = -1
    
    for start_x in range(N):
        for start_y in range(M):
            
            for dx in range(-N, N):
                for dy in range(-M, M):
                    
                    if dx == 0 and dy == 0:
                        continue
                    
                    num = ''
                    x, y = start_x, start_y
                    while 0 <= x < N and 0 <= y < M:
                        num += grid[x][y]
                        num_int = int(num)
                        if is_perfect_square(num_int):
                            max_square = max(max_square, num_int)
                        x += dx
                        y += dy
    return max_square
print(sol(N=N, M=M, grid=grid))
                        
                        
                            