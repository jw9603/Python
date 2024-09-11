# 네 번째 점 3009
# https://www.acmicpc.net/problem/3009

import sys
from collections import Counter
w = []
h = []
for _ in range(3):
    x, y = map(int,sys.stdin.readline().split())
    w.append(x)
    h.append(y)

for i in range(3):
    if w.count(w[i]) == 1:
        x = w[i]
    if h.count(h[i]) == 1:
        y = h[i]
print(x,y)

