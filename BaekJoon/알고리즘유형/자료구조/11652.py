# 백준 11652. 카드
# https://www.acmicpc.net/problem/11652
import sys
from collections import Counter
N = int(sys.stdin.readline().strip())
cards = [int(sys.stdin.readline().strip()) for _ in range(N)]
def sol(cards):
    cards_count = Counter(cards)
    cards_count = sorted(cards_count.items(), key=lambda x:(-x[1],x[0]))
    return cards_count[0][0]
print(sol(cards=cards))
