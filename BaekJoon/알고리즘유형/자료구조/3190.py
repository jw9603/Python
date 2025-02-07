# 백준 3190. 뱀
# https://www.acmicpc.net/problem/3190
import sys
from collections import deque
N = int(sys.stdin.readline().strip()) # 보드의 크기
k = int(sys.stdin.readline().strip()) # 사과의 개수
apples = [tuple(map(int, sys.stdin.readline().split())) for _ in range(k)] # (x, y)좌표
L = int(sys.stdin.readline().strip())
directions = [tuple(sys.stdin.readline().split()) for _ in range(L)] # (X, C): 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽 또는 오른쪽으로 90도 방향 회전
directions = [(int(x), d) for x, d in directions]

def sol(N, apples, directions):
    # 동, 남, 서, 북
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    board = [[0] * N for _ in range(N)]
    # 보드의 시작은 (1, 1) 즉 (0, 0) 이 아님
    # 사과의 위치를 1로 지정
    for x, y in apples:
        board[x - 1][y - 1] = 1
    
    snake = deque([(0, 0)])
    time = 0
    direction = 0 # 초기 방향(동쪽)
    
    # 뱀의 방향 변환 정보
    direction_change = {}
    for x, d in directions:
        direction_change[x] = d
    
    while True:
        time += 1
        head_x, head_y = snake[-1] # 현재 머리 위치
        
        # 몸길이를 늘려 머리를 다음칸에 위치 시킨다.
        nx = head_x + dx[direction]
        ny = head_y + dy[direction]
        
        # 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
        if nx < 0 or nx >= N or ny < 0 or ny >= N or (nx, ny) in snake:
            return time
        
        snake.append((nx, ny))
        
        # 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다.
        if board[nx][ny] == 0:
            snake.popleft()
        else:
            # 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
            board[nx][ny] = 0
        
        if time in direction_change:
            turn = direction_change[time]
            
            if turn == 'L': # 왼쪽으로 회전
                direction = (direction - 1) % 4
            else:           # 오른쪽으로 회전
                direction = (direction + 1) % 4
    
print(sol(N=N, apples=apples, directions=directions))
        
        
        
    