# 백준 1726. 로봇
# https://www.acmicpc.net/problem/1726
import sys
from collections import deque
def bfs(factory, M, N, start, end):
    # 동, 남, 서 북
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_map = {1: 0, 3: 1, 2: 2, 4: 3}
    visited = [[[False] * 4 for _ in range(N)] for _ in range(M)]

    sx, sy, sd = start
    ex, ey, ed = end
    sd = dir_map[sd]
    ed = dir_map[ed]

    queue = deque([(sx, sy, sd, 0)])
    visited[sx][sy][sd] = True

    while queue:
        cur_x, cur_y, cur_d, cur_cnt = queue.popleft()

        if (cur_x, cur_y, cur_d) == (ex, ey, ed):
            return cur_cnt
        
        for k in range(1, 4):
            next_x = cur_x + directions[cur_d][0] * k
            next_y = cur_y + directions[cur_d][1] * k

            if 0 <= next_x < M and 0 <= next_y < N and factory[next_x][next_y] == 0:
                if not visited[next_x][next_y][cur_d]:
                    visited[next_x][next_y][cur_d] = True
                    queue.append((next_x, next_y, cur_d, cur_cnt + 1))
            else:
                break

        for next_d in [(cur_d + 1) % 4, (cur_d + 3) % 4]:
            if not visited[cur_x][cur_y][next_d]:
                visited[cur_x][cur_y][next_d] = True
                queue.append((cur_x, cur_y, next_d, cur_cnt + 1))
        
def main():
    M, N = map(int, sys.stdin.readline().split())
    factory = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

    sx, sy, sd = map(int, sys.stdin.readline().split())
    ex, ey, ed = map(int, sys.stdin.readline().split())
    sx -= 1
    sy -= 1
    ex -= 1
    ey -= 1

    print(bfs(factory, M, N, (sx, sy, sd), (ex, ey, ed)))

if __name__ == '__main__':
    main()