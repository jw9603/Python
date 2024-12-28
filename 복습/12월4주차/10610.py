# 백준 10610. 30
# https://www.acmicpc.net/problem/10610
import sys
N = sys.stdin.readline().strip()
def sol(N):
    if '0' not in N or len(N) == 1:
        return -1
    if sum(map(int, N)) % 3 != 0:
        return -1
    return ''.join(sorted(N, reverse=True))
print(sol(N=N))
    