# 백준 15686. 치킨 배달
# https://www.acmicpc.net/problem/15686
################################## 백트래킹 ##################################
import sys
def calculate_chicken_dist(houses, selected):
    total_dist = 0

    for hx, hy in houses:
        min_distance = float('inf')
        for cx, cy in selected:
            min_distance = min(min_distance, abs(hx - cx) + abs(hy - cy))
        total_dist += min_distance
    
    return total_dist

def backtrack(start, selected, houses, chickens, M):
    global min_dist

    if len(selected) == M:
        city_distance = calculate_chicken_dist(houses, selected)
        min_dist = min(min_dist, city_distance)
        return
    
    for i in range(start, len(chickens)):
        selected.append(chickens[i])
        backtrack(i + 1, selected, houses, chickens, M)
        selected.pop()

def sol(N, M, city):
    global min_dist
    min_dist = float('inf')
    houses = []
    chickens = []

    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                houses.append((i, j))
            elif city[i][j] == 2:
                chickens.append((i, j))
    
    backtrack(0, [], houses, chickens, M)

    return min_dist

def main():
    N, M = map(int, sys.stdin.readline().split())
    city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    print(sol(N, M, city))

if __name__ == '__main__':
    main()
################################## 백트래킹 ##################################

################################## itertools ##################################
import sys
from itertools import combinations
def calculate_chicken_dist(houses, selected):
    total_dist = 0

    for hx, hy in houses:
        min_distance = float('inf')
        for cx, cy in selected:
            min_distance = min(min_distance, abs(hx - cx) + abs(hy - cy))
        total_dist += min_distance
    
    return total_dist

def sol(N, M, city):
    min_dist = float('inf')
    houses = []
    chickens = []

    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                houses.append((i, j))
            elif city[i][j] == 2:
                chickens.append((i, j))
    
    for selected in combinations(chickens, M):

        city_distance = calculate_chicken_dist(houses, selected)
        min_dist = min(city_distance, min_dist)

    return min_dist

def main():
    N, M = map(int, sys.stdin.readline().split())
    city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    print(sol(N, M, city))

if __name__ == '__main__':
    main()
################################## itertools ##################################