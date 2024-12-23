# 백준 13305번. 주유소
# https://www.acmicpc.net/problem/13305
import sys
N = int(sys.stdin.readline().strip())
roads = list(map(int, sys.stdin.readline().split()))
prices = list(map(int, sys.stidn.readline().split()))

def sol(n, roads, prices):
    result = 0
    min_price = prices[0]
    for i in range(n - 1):
        if min_price > prices[i]:
            min_price = prices[i]
        result += min_price * roads[i]
    print(result)
sol(n=N, roads=roads, prices=prices)