# 백준 11399. ATM
# https://www.acmicpc.net/problem/11399
import sys
N = int(sys.stdin.readline().strip())
times = sorted([*map(int, sys.stdin.readline().split())])
def sol(times):
    total_time = 0
    cul_time = 0
    for time in times:
        cul_time += time
        total_time += cul_time
    return total_time
print(sol(times=times))
