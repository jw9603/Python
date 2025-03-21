# 백준 2146. 다리 만들기
# https://www.acmicpc.net/problem/2146
import sys
from collections import deque

def check_island(x, y, board, id):
    global N
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    queue.append((x, y))
    board[x][y] = id

    while queue:
        cur_x, cur_y = queue.popleft()

        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy
            if 0 <= next_x < N and 0 <= next_y < N and board[next_x][next_y] == 1:
                board[next_x][next_y] = id
                queue.append((next_x, next_y))

def build_bridge(island_num):
    global N, board
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[-1] * N for _ in range(N)]
    queue = deque()

    for i in range(N):
        for j in range(N):
            if board[i][j] == island_num:
                visited[i][j] = 0
                queue.append((i, j))

    min_dist = float('inf')
    
    while queue:
        cur_x, cur_y = queue.popleft()

        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy
            
            if 0 <= next_x < N and 0 <= next_y < N:

                if board[next_x][next_y] != 0 and board[next_x][next_y] != island_num:
                    return visited[cur_x][cur_y]
                if board[next_x][next_y] == 0 and visited[next_x][next_y] == -1:
                    visited[next_x][next_y] = visited[cur_x][cur_y] + 1
                    queue.append((next_x, next_y))

    return float('inf')

def main():
    global N, board
    N = int(sys.stdin.readline().strip())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    # 0: 바다, 1: 육지, 2이상: 섬

    island_id = 2

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                check_island(i, j, board, island_id)
                island_id += 1
    

    min_bridge = float('inf')
    for i in range(2, island_id):
        min_bridge = min(min_bridge, build_bridge(i))
    
    print(min_bridge)

if __name__ == '__main__':
    main()