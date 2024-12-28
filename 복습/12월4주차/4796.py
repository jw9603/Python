# 백준 4796. 캠핑
# https://www.acmicpc.net/problem/4796
import sys
i = 1
while 1:
    L, P, V = map(int, sys.stdin.readline().split())
    if L == 0 and P == 0 and V == 0:
            break
    result = (V // P) * L + min(V % P, L)
    print(f"Case {i}: {result}")
    i += 1