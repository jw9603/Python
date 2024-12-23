# 백준 1789. 수들의 합
# https://www.acmicpc.net/problem/1789
import sys
S = int(sys.stdin.readline().strip())
def sol(S):
    N = 0
    total = 0
    while total + N + 1 <= S:
        N += 1
        total += N
    return N
print(sol(S=S))