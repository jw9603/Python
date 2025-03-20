# 백준 1600. 말이 되고픈 원숭이
# https://www.acmicpc.net/problem/1600
import sys
from collections import deque
def min_monkey_move(K, W, H, grid):
    visited = [[[False] * (K + 1) for _ in range(W)] for _ in range(H)]

    queue = deque([(0, 0, 0, 0)]) # x, y, 사용한 k, 이동 횟수
    visited[0][0][0] = True

    horse_directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    monkey_directions = [(-1, 0), (1, 0), (0 ,-1), (0, 1)]

    while queue:
        cur_x, cur_y, used_k, cur_steps = queue.popleft()

        if cur_x == H - 1 and cur_y == W - 1:
            return cur_steps
        
        for dx, dy in monkey_directions:
            next_x, next_y = cur_x + dx, cur_y + dy
            if 0 <= next_x < H and 0 <= next_y < W and not visited[next_x][next_y][used_k] and grid[next_x][next_y] == 0:
                visited[next_x][next_y][used_k] = True
                queue.append((next_x, next_y, used_k, cur_steps + 1))
            
        if used_k < K:
            for dx, dy in horse_directions:
                next_x, next_y = cur_x + dx, cur_y + dy
                if 0 <= next_x < H and 0 <= next_y < W and not visited[next_x][next_y][used_k + 1] and grid[next_x][next_y] == 0:
                    visited[next_x][next_y][used_k + 1] = True
                    queue.append((next_x, next_y, used_k + 1, cur_steps + 1))
    return -1
        
def main():
    K = int(sys.stdin.readline().strip())
    W, H = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]

    print(min_monkey_move(K, W, H, grid))

if __name__ == '__main__':
    main()