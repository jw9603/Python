# 백준 5568. 카드 놓기
# https://www.acmicpc.net/problem/5568
import sys
from itertools import permutations
n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
cards = [sys.stdin.readline().strip() for _ in range(n)]
print(len(set(''.join(i) for i in permutations(cards, k))))



############################ 재귀 방법 ##########################
import sys
n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
cards = [sys.stdin.readline().strip() for _ in range(n)]

def generate_numbers(cards, k, current, result):
    if len(current) == k:
        result.add(''.join(map(str, current)))
        return
        
    for i in range(len(cards)):
        # print(f"재귀 호출: current={current + [cards[i]]}, remaining={cards[:i] + cards[i+1:]}")
        generate_numbers(cards[:i] + cards[i + 1:], k, current + [cards[i]], result)


def unique_numbers(cards, k):
    result = set()
    generate_numbers(cards=cards, k=k, current=[], result=result)
    print(len(result))
unique_numbers(cards=cards, k=k)
############################ 재귀 방법 ##########################