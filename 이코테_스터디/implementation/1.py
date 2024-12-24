# 예제 4 - 1 상하좌우
import sys
N = int(sys.stdin.readline().strip())
moves = sys.stdin.readline().split()

directions = [(0, -1), (0, 1), (-1, 0), (1, 0)] # L, R, U, D
move_types = ['L', 'R', 'U', 'D']
x, y = 1, 1
for move in moves: # R R R U D
    for i in range(len(move_types)):
        if move == move_types[i]:
            nx = x + directions[i][0]
            ny = y + directions[i][1]
    
    if nx < 1 or nx > N or ny < 1 or ny > N:
        continue
    x, y = nx, ny
print(x, y)
    