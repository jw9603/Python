# 백준 15686. 치킨 배달
# https://www.acmicpc.net/problem/15686
def calculate_chicken_distance(houses, selected):
    total_distance = 0

    for hx, hy in houses:
        cur_distance = float('inf')
        for cx, cy in selected:
            cur_distance = min(cur_distance, abs(hx - cx) + abs(hy - cy))
        total_distance += cur_distance
    
    return total_distance

def dfs(start, selected, houses, chickens, M):
    global min_distance

    if len(selected) == M:
        chicken_distance = calculate_chicken_distance(houses, selected)
        min_distance = min(min_distance, chicken_distance)
        return
    
    for i in range(start, len(chickens)):
        selected.append(chickens[i])
        dfs(i + 1, selected, houses, chickens, M)
        selected.pop()

def sol(N, M, city):
    global min_distance
    min_distance = float('inf')

    houses, chickens = [], []

    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                houses.append((i, j))
            elif city[i][j] == 2:
                chickens.append((i, j))
    
    dfs(0, [], houses, chickens, M)

    return min_distance

def main():
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]

    print(sol(N, M, city))
    
if __name__ == '__main__':
    main()