# 백준 15903. 카드 합체 놀이
# https://www.acmicpc.net/problem/15903
import sys
from heapq import heappop, heappush, heapify
n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
def sol(m, cards):
    heapify(cards)
    for _ in range(m):
        x = heappop(cards)
        y = heappop(cards)
        new_val = x + y
        heappush(cards, new_val)
        heappush(cards, new_val)
    return sum(cards)
print(sol(m=m, cards=cards))
    