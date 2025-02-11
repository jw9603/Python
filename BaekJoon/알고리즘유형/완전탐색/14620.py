# 백준 14620. 꽃길
# https://www.acmicpc.net/problem/14620
import sys
from itertools import combinations
N = int(sys.stdin.readline().strip())
garden = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def sol(N, garden):
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]

    possible_positions = [(x, y) for x in range(1, N - 1) for y in range(1, N - 1)]

    min_cost = float('inf')

    for seeds in combinations(possible_positions, 3):
        total_cost = 0
        visited = set()
        valid = True
        for x, y in seeds:
            flower_cost = 0
            flower_positions = []
            for d in range(5): # 꽃술 + 4방향 탐색
                nx, ny = x + dx[d], y + dy[d]
                
                if (nx, ny) in visited:
                    valid = False
                    break
                visited.add((nx, ny))
                flower_cost += garden[nx][ny]
                flower_positions.append((nx, ny))
            
            if not valid:
                break
            total_cost += flower_cost
        if valid:
            min_cost = min(min_cost, total_cost)

    print(min_cost)    

sol(N=N, garden=garden)