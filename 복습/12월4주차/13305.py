# 백준 13305. 주유소
# https://www.acmicpc.net/problem/13305
import sys
N = int(sys.stdin.readline().strip())                # 4
roads = list(map(int, sys.stdin.readline().split())) # 2 3 1
oils = list(map(int, sys.stdin.readline().split()))  # 5 2 4 1
def sol(N, roads, oils):
    
    min_price = oils[0]
    result = 0
    for i in range(N - 1):
        if min_price > oils[i]:
            min_price = oils[i]
        result += min_price * roads[i]
    print(result)
sol(N=N, roads=roads, oils=oils)        