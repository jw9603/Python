# 백준 7569. 토마토
# https://www.acmicpc.net/problem/7569
import sys
from collections import deque

def bfs_3d(M, N, H, box):
    directions = [
        (1, 0, 0),
        (-1, 0, 0),
        (0, -1, 0),
        (0, 1, 0),
        (0, 0, -1),
        (0, 0, 1)
    ]

    queue = deque()
    unripe_cnt = 0
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if box[h][n][m] == 1:
                    queue.append((h, n, m, 0))
                elif box[h][n][m] == 0:
                    unripe_cnt += 1
    if unripe_cnt == 0:
        return 0
    
    result = 0

    while queue:
        cur_h, cur_x, cur_y, cur_t = queue.popleft()
        result = max(result, cur_t)

        for dh, dx, dy in directions:
            next_h, next_x, next_y = cur_h + dh, cur_x +dx, cur_y + dy

            if 0 <= next_h < H and 0 <= next_x < N and 0 <= next_y < M:
                if box[next_h][next_x][next_y] == 0:
                    box[next_h][next_x][next_y] = 1
                    unripe_cnt -= 1
                    queue.append((next_h, next_x, next_y, cur_t + 1))
    return result if not unripe_cnt else -1

def main():
    M, N, H = map(int, sys.stdin.readline().split())
    box = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

    print(bfs_3d(M, N, H, box))

if __name__ == '__main__':
    main()