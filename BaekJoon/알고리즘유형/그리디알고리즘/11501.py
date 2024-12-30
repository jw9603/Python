# 백준 11501. 주식
# https://www.acmicpc.net/problem/11501
import sys
def sol(prices):
    profit = 0
    max_profit = 0
    for price in reversed(prices):
        if price > max_profit:
            max_profit = price
        else:
            profit += max_profit - price
    return profit

T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    prices = list(map(int, sys.stdin.readline().split()))
    print(sol(prices=prices))