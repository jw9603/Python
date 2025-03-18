# 백준 14503. 로봇 청소기
# https://www.acmicpc.net/problem/14503
import sys
def clean_rooms(N, M, r, c, d, grid):
    # 북, 동, 남, 서
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    visited = [[False] * M for _ in range(N)]
    visited[r][c] = True
    cnt = 1

    while True:
        found = False

        for _ in range(4):
            d = (d + 3) % 4
            next_r, next_c = r + dr[d], c + dc[d]

            if 0 <= next_r < N and 0 <= next_c < M and grid[next_r][next_c] == 0 and not visited[next_r][next_c]:
                visited[next_r][next_c] = True
                cnt += 1
                r, c = next_r, next_c
                found = True
                break

        if not found:
            next_r, next_c = r - dr[d], c - dc[d]
            if 0 <= next_r < N and 0 <= next_c < M and grid[next_r][next_c] == 0:
                r, c = next_r, next_c
            else:
                return cnt

def main():
    N, M = map(int, sys.stdin.readline().split())
    r, c, d = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    print(clean_rooms(N, M, r, c, d, grid))

if __name__ == '__main__':
    main()