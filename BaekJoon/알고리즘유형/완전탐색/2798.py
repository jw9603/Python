# 백준 2798. 블랙잭
# https://www.acmicpc.net/problem/2798
import sys
from itertools import combinations
N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
def sol(M, cards):
    shortest_sum = 9
    for comb in combinations(cards, 3):
        if M >= sum(comb) and sum(comb) > shortest_sum:
            shortest_sum = sum(comb)
    return shortest_sum
print(sol(M=M, cards=cards))
        
