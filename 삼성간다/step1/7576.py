# 백준 7576. 토마토
# https://www.acmicpc.net/problem/7576
import sys
from collections import deque
def bfs(M, N, boxes):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque()
    unripe_cnt = 0

    for i in range(N):
        for j in range(M):
            if boxes[i][j] == 1:
                queue.append((i, j, 0))
            elif boxes[i][j] == 0:
                unripe_cnt += 1
    result = 0
    while queue:
        cur_x, cur_y, cur_day = queue.popleft()
        result = max(result, cur_day)
        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy

            if 0 <= next_x < N and 0 <= next_y < M:
                if boxes[next_x][next_y] == 0:
                    boxes[next_x][next_y] = 1
                    unripe_cnt -= 1
                    queue.append((next_x, next_y, cur_day + 1))
    return result if not unripe_cnt else -1
        
def main():
    M, N = map(int, sys.stdin.readline().split())
    boxes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    print(bfs(M, N, boxes))

if __name__ == '__main__':
    main()