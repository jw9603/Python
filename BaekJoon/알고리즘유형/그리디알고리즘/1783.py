# 백준 1783. 병든 나이트
# https://www.acmicpc.net/problem/1783
import sys
N, M = map(int, sys.stdin.readline().split())
def sol(N, M):
    if N == 1:
        return 1
    elif N == 2:
        return min(4, (M + 1) // 2)
    elif M < 7:
        return min(4, M)
    else:
        return M - 2
print(sol(N=N, M=M))