# 2164 카드 2
# https://www.acmicpc.net/problem/2164

import sys
from collections import deque

N = int(sys.stdin.readline().strip())

card = deque([i for i in range(1,N+1)])

while len(card) > 1:
    card.popleft()
    card.append(card.popleft())

print(card[0])