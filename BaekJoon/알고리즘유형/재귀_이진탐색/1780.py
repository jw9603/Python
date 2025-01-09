# 백준 1780. 종이의 개수 
# https://www.acmicpc.net/problem/1780
#  N은 3^k 꼴이다.
import sys
N = int(sys.stdin.readline().strip())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cnt1_, cnt0, cnt1 = 0, 0, 0

def sol(matrix, x, y, size):
    global cnt1_, cnt0, cnt1
    
    first_val = matrix[x][y]
    is_same = True
    for i in range(x, x + size):
        for j in range(y, y + size):
            if matrix[i][j] != first_val:
                is_same = False
                break
        if not is_same:
            break
    
    if is_same:
        if first_val == -1:
            cnt1_ += 1
        elif first_val == 0:
            cnt0 += 1
        else:
            cnt1 += 1
    else:
        next_size = size // 3
        for i in range(3):
            for j in range(3):
                sol(matrix, x + i * next_size, y + j * next_size, next_size)

sol(matrix, 0, 0, N)
print(cnt1_, cnt0, cnt1, sep='\n')