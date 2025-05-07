# 백준 7569. 토마토
# https://www.acmicpc.net/problem/7569
################################ 문제 이해 ################################
# 높이 H, 가로 M, 세로 N
# 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
# 인접한 곳은 상하좌우,위, 아래로 6방향
# 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 그 최소 일수를 구해라.
# 1: 익은 토마토, 0: 익지 않은 토마토
# 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을
# 받아 익게 된다.
################################ 문제 이해 ################################
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
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if box[i][j][k] == 1:
                    queue.append((i, j, k, 0))
                elif box[i][j][k] == 0:
                    unripe_cnt += 1

    if unripe_cnt == 0:
        return 0
    
    result = 0

    while queue:
        cur_h, cur_x, cur_y, cur_t = queue.popleft()
        result = max(result, cur_t)

        for dh, dx, dy in directions:
            next_h, next_x, next_y = cur_h + dh, cur_x + dx, cur_y + dy

            if 0 <= next_h < H and 0 <= next_x < N and 0 <= next_y < M:
                if box[next_h][next_x][next_y] == 0:
                    unripe_cnt -= 1
                    box[next_h][next_x][next_y] = 1
                    queue.append((next_h, next_x, next_y, cur_t + 1))

    return result if not unripe_cnt else -1

def main():
    M, N, H = map(int, input().split())
    box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

    print(bfs_3d(M, N, H, box))

if __name__ == '__main__':
    main()