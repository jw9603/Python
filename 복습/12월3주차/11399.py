# 백준 11399. ATM
# https://www.acmicpc.net/problem/11399
import sys
N = int(sys.stdin.readline().strip())
times = sorted(list(map(int, sys.stdin.readline().split())))
def sol(times):
    total = 0
    tmp = 0
    for t in times:
        tmp += t
        total += tmp
    print(total)
sol(times=times)
        
