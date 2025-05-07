# 백준 2665. 미로만들기
# https://www.acmicpc.net/problem/2665
################################ 문제 이해 ################################
# n x n 바둑판, 일부분은 검은방, 나머지는 흰 방
# 검은 방은 들어갈 수 없다. 흰방끼리는 이동 가능 (상하좌우)
# 0: 검은 방, 1: 흰 방
################################ 문제 이해 ################################
from collections import deque
def sol(n, grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(0, 0, 0)])
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True

    while queue:
        cur_x, cur_y, cur_t = queue.popleft()

        if cur_x == n - 1 and cur_y == n - 1:
            return cur_t
        
        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy

            if 0 <= next_x < n and 0 <= next_y < n:
                if not visited[next_x][next_y]:
                    visited[next_x][next_y] = True

                    if grid[next_x][next_y] == 0:
                        queue.append((next_x, next_y, cur_t + 1))
                    else:
                        queue.appendleft((next_x, next_y, cur_t))

def main():
    n = int(input().strip())
    grid = [list(map(int, input().strip())) for _ in range(n)]

    print(sol(n, grid))

if __name__ == '__main__':
    main()