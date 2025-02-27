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
    
################################## 백트래킹 ###################################
import sys

def calculate_chicken_distance(houses, selected_chicken):
    """선택된 치킨집들에 대해 도시의 치킨 거리를 계산하는 함수"""
    total_distance = 0
    for hx, hy in houses:
        min_distance = float('inf')
        for cx, cy in selected_chicken:
            min_distance = min(min_distance, abs(hx - cx) + abs(hy - cy))
        total_distance += min_distance
    return total_distance

def backtrack(idx, selected, houses, chickens, M):
    """백트래킹을 이용해 치킨집을 선택하는 함수"""
    global min_distance
    
    # M개의 치킨집을 선택한 경우, 최소 치킨 거리 갱신
    if len(selected) == M:
        city_distance = calculate_chicken_distance(houses, selected)
        min_distance = min(min_distance, city_distance)
        return
    
    # 백트래킹 탐색 (idx부터 탐색하여 중복 방지)
    for i in range(idx, len(chickens)):
        selected.append(chickens[i])
        backtrack(i + 1, selected, houses, chickens, M)
        selected.pop()  # 백트래킹

def sol(N, M, city):
    """도시 정보를 받아서 최소 치킨 거리를 구하는 함수"""
    global min_distance
    min_distance = float('inf')
    
    houses = []
    chickens = []
    
    # 집과 치킨집 위치 찾기
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                houses.append((i, j))
            elif city[i][j] == 2:
                chickens.append((i, j))
    
    # 백트래킹 시작
    backtrack(0, [], houses, chickens, M)
    
    return min_distance

def main():
    N, M = map(int, sys.stdin.readline().split())
    city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    print(sol(N=N, M=M, city=city))

main()
################################## 백트래킹 ###################################
