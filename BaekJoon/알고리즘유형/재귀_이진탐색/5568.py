# 백준 5568. 카드 놓기
# https://www.acmicpc.net/problem/5568
# 해당 문제는 순열을 통해 쉽게 풀 수 있다.
#################### 순열 풀이 #####################
import sys
from itertools import permutations
n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
cards = [sys.stdin.readline().strip() for _ in range(n)]
print(len(set(''.join(i) for i in permutations(cards, k))))
#################### 순열 풀이 #####################

######################## 재귀 풀이 #########################
import sys
from itertools import permutations
n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
cards = [int(sys.stdin.readline().strip()) for _ in range(n)]

def sol(cards, k, current, result):
    # 1. base case
    if len(current) == k:
        result.add(''.join(map(str, current)))
        return
    # 2. 재귀 호출: 지금 뽑은게 current, 나머지것들이 cards
    for i in range(len(cards)):
        sol(cards[:i] + cards[i + 1:], k, current + [cards[i]], result)

result = set()
sol(cards=cards, k=k, current=[], result=result)
print(len(result))
######################## 재귀 풀이 #########################