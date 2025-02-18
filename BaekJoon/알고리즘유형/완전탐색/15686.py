# 백준 15686. 치킨 배달
# https://www.acmicpc.net/problem/15686
import sys
from itertools import combinations
def calculate_chicken_distance(houses, selected_chicken):
    
    total_distance = 0
    
    for hx, hy in houses:
        min_distance = float('inf')
        for cx, cy in selected_chicken:
            min_distance = min(min_distance, abs(hx - cx) + abs(hy - cy))
        total_distance += min_distance
    return total_distance

def sol(N, M, city):
    houses = []
    chickens = []
    for r in range(N):
        for c in range(N):
            if city[r][c] == 1:
                houses.append((r, c))
            elif city[r][c] == 2:
                chickens.append((r, c))
    
    min_distance = float('inf')
    
    for selected_chicken in combinations(chickens, M):
        
        city_distance = calculate_chicken_distance(houses, selected_chicken)
        min_distance = min(city_distance, min_distance)
    return min_distance
                
def main():
    N, M = map(int, sys.stdin.readline().split())
    city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    print(sol(N=N, M=M, city=city))

if __name__ == '__main__':
    main()
    
