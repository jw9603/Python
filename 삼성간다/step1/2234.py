# 백준 2234. 성곽
# https://www.acmicpc.net/problem/2234
import sys
from collections import deque
def bfs(x, y, room_id, grid, visited, room_map, room_sizes):
    global wall_table

    n, m = len(grid), len(grid[0])
    # 서, 북, 동, 남
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    queue = deque([(x, y)])
    visited[x][y] = True
    room_map[x][y] = room_id
    size = 1

    while queue:
        cur_x, cur_y = queue.popleft()

        for idx, (dx, dy) in enumerate(directions):
            next_x, next_y = cur_x + dx, cur_y + dy

            if 0 <= next_x < n and 0 <= next_y < m:

                if not visited[next_x][next_y] and wall_table[grid[cur_x][cur_y]][idx] == 0:
                    visited[next_x][next_y] = True
                    room_map[next_x][next_y] = room_id
                    queue.append((next_x, next_y))
                    size += 1
    room_sizes[room_id] = size
    return size


def solve_castle_problem(N, M, grid):
    visited = [[False] * N for _ in range(M)]
    room_map = [[-1] * N for _ in range(M)]

    room_cnt = 0
    room_sizes = {}
    max_room = 0
    max_merge = 0
    
    # 1. 이 성에 있는 방의 개수
    for i in range(M):
        for j in range(N):
            if not visited[i][j]:
                room_cnt += 1
                size = bfs(i, j, room_cnt, grid, visited, room_map, room_sizes)
                max_room = max(max_room, size)
    
    # 2. 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기
    directions = [(0, 1), (1, 0)] # 동, 남
    for x in range(M):
        for y in range(N):
            for dx, dy in directions:
                next_x, next_y = x + dx, y + dy
                if 0 <= next_x < M and 0 <= next_y < N:
                    r1, r2 = room_map[x][y], room_map[next_x][next_y]

                    if r1 != r2:
                        max_merge = max(max_merge, room_sizes[r1] + room_sizes[r2])
    return room_cnt, max_room, max_merge

def main():
    global wall_table
    N, M = map(int, sys.stdin.readline().split())

    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

    # 벽 정보 테이블: 각 정수에 대한 [서, 북, 동, 남] 방향 벽 유무
    wall_table = {
        0: [0, 0, 0, 0],
        1: [1, 0, 0, 0],
        2: [0, 1, 0, 0],
        3: [1, 1, 0, 0],
        4: [0, 0, 1, 0],
        5: [1, 0, 1, 0],
        6: [0, 1, 1, 0],
        7: [1, 1, 1, 0],
        8: [0, 0, 0, 1],
        9: [1, 0, 0, 1],
        10: [0, 1, 0, 1],
        11: [1, 1, 0, 1],
        12: [0, 0, 1, 1],
        13: [1, 0, 1, 1],
        14: [0, 1, 1, 1],
        15: [1, 1, 1, 1],
    }

    result = solve_castle_problem(N, M, grid)
    print(*result, sep='\n')

if __name__ == '__main__':
    main()