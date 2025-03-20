# 백준 3190. 뱀
# https://www.acmicpc.net/problem/3190
import sys
from collections import deque
def game_over_time(N, apples, directions):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    board = [[0] * N for _ in range(N)]
    for x, y in apples:
        board[x - 1][y - 1] = 1
    
    time = 0
    snake = deque([(0, 0)])
    direction = 0

    directions_info = {}
    for x, d in directions:
        directions_info[x] = d
    
    while True:
        time += 1
        head_x, head_y = snake[-1]

        next_x, next_y = head_x + dx[direction], head_y + dy[direction]

        if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N or (next_x, next_y) in snake:
            return time

        snake.append((next_x, next_y))

        if board[next_x][next_y] == 1:
            board[next_x][next_y] = 0
        else:
            snake.popleft()
        
        if time in directions_info:
            turn = directions_info[time]

            if turn == 'L':
                direction = (direction - 1) % 4
            else:
                direction = (direction + 1) % 4

def main():
    N = int(sys.stdin.readline().strip())
    K = int(sys.stdin.readline().strip())
    apples = [tuple(map(int, sys.stdin.readline().split())) for _ in range(K)]
    L = int(sys.stdin.readline().strip())
    directions = [tuple(sys.stdin.readline().split()) for _ in range(L)]
    directions = [(int(x), d) for x, d in directions]

    print(game_over_time(N, apples, directions))

if __name__ == '__main__':
    main()