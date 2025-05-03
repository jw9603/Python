# 백준 7576. 토마토
# https://www.acmicpc.net/problem/7576
############################### 문제 이해 ###############################
# 가로: M, 세로: N의 창고가 있다.
# 창고에는 익은 토마토도 있고 안익은 토마토도 있다.
# 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받는다.
# 인접하다 == 상하좌우, 
# 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되냐? 
# 1: 익은 토마토, 0: 익지 않은 토마토
############################### 문제 이해 ###############################
from collections import deque
def solve(N, M, grid):
    queue = deque()
    unripe_cnt = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                queue.append((i, j, 0))
            elif grid[i][j] == 0:
                unripe_cnt += 1

    if not unripe_cnt:
        return 0
    
    result = 0

    while queue:
        cur_x, cur_y, cur_t = queue.popleft()

        result = max(cur_t, result)

        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy
            if 0 <= next_x < N and 0 <= next_y < M:
                if grid[next_x][next_y] == 0:
                    grid[next_x][next_y] = 1
                    unripe_cnt -= 1
                    queue.append((next_x, next_y, cur_t + 1))

    return result if  not unripe_cnt else -1

def main():
    M, N = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    print(solve(N, M, grid))

if __name__ == '__main__':
    main()