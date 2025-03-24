# 백준 19238. 스타트 택시
# https://www.acmicpc.net/problem/19238
import sys
from collections import deque

def find_nearest_passenger(N, grid, start, passengers, fuel):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[-1] * N for _ in range(N)]
    queue = deque([start])
    visited[start[0]][start[1]] = 0

    candidates = []

    while queue:
        cur_x, cur_y = queue.popleft()

        if (cur_x, cur_y) in passengers:
            candidates.append((visited[cur_x][cur_y], cur_x, cur_y))

        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy

            if 0 <= next_x < N and 0 <= next_y < N:
                if grid[next_x][next_y] == 0 and visited[next_x][next_y] == -1:
                    visited[next_x][next_y] = visited[cur_x][cur_y] + 1
                    queue.append((next_x, next_y))
    
    if not candidates:
        return None, -1
    
    candidates.sort()
    dist, px, py = candidates[0]

    if dist > fuel:
        return None, -1
    
    return (px, py), dist

def move_to_destination(N, passenger_start, passenger_dest, grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[-1] * N for _ in range(N)]
    queue = deque([passenger_start])
    visited[passenger_start[0]][passenger_start[1]] = 0

    while queue:
        cur_x, cur_y = queue.popleft()

        if (cur_x, cur_y) == passenger_dest:
            return visited[cur_x][cur_y]
        
        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy

            if 0 <= next_x < N and 0 <= next_y < N:
                if grid[next_x][next_y] == 0 and visited[next_x][next_y] == -1:
                    visited[next_x][next_y] = visited[cur_x][cur_y] + 1
                    queue.append((next_x, next_y))
    return -1

def main():
    N, M, fuel = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    sx, sy = map(int, sys.stdin.readline().split())
    
    passengers = {}

    for _ in range(M): # M: 승객
        a, b, c, d = map(int, sys.stdin.readline().split())
        passengers[(a - 1, b - 1)] = (c - 1, d - 1)
    
    taxi_position = (sx - 1, sy - 1)

    for _ in range(M):
        passenger_start, dist_to_passenger = find_nearest_passenger(N, grid, taxi_position, passengers, fuel)
        
        if passenger_start is None:
            print(-1)
            return
        
        fuel -= dist_to_passenger
        if fuel < 0:
            print(-1)
            return
        
        # 목적지까지 이동
        passenger_dest = passengers[passenger_start]
        dist_to_dest = move_to_destination(N, passenger_start, passenger_dest, grid)

        if dist_to_dest == -1 or fuel < dist_to_dest:
            print(-1)
            return
        
        fuel = fuel - dist_to_dest + (dist_to_dest) * 2
        taxi_position = passenger_dest

        del passengers[passenger_start]
    
    print(fuel)

if __name__ == '__main__':
    main()