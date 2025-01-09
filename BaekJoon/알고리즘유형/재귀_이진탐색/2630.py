# 백준 2630. 색종이 만들기
# https://www.acmicpc.net/problem/2630
import sys
N = int(sys.stdin.readline().strip())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def sol(matrix, x, y, size):
    global cntw, cntb
    
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
        if first_val == 0:
            cntw += 1
        else:
            cntb += 1
    else:
        new_size = size // 2
        
        ##################### 이 부분은 교체될 수 있음 #######################
        for i in range(2):
            for j in range(2):
                sol(matrix, x + new_size * i, y + new_size * j, new_size)
        ##################### 이 부분은 교체될 수 있음 #######################
        
        ##################### 이 부분은 교체될 수 있음 #######################
        # sol(matrix, x, y, new_size)
        # sol(matrix, x, y + new_size, new_size)
        # sol(matrix, x + new_size, y, new_size)
        # sol(matrix, x + new_size, y + new_size, new_size)
        ##################### 이 부분은 교체될 수 있음 #######################

cntw, cntb = 0, 0
sol(matrix, 0, 0, N)
print(cntw, cntb, sep='\n')