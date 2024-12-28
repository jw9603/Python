# 백준 1074. Z
# https://www.acmicpc.net/problem/1074
import sys
N, r, c = map(int, sys.stdin.readline().split())
def sol(n, r, c):
    if n == 0:
        return 0
    size = 2 ** (n - 1)
    cnt = size ** 2
    
    if r < size and c < size: # 1사분면
        return sol(n - 1, r, c)
    elif r < size and c >= size: # 2사분면
        return cnt + sol(n - 1, r, c - size)
    elif r >= size and c < size: # 3사분면
        return 2 * cnt + sol(n - 1, r - size, c)
    else: # 4사분면
        return 3 * cnt + sol(n - 1, r - size, c - size)
print(sol(n=N, r=r, c=c))