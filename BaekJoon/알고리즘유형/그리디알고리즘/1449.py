# 백준 1449. 수리공 항승
# https://www.acmicpc.net/problem/1449
import sys
N, L = map(int, sys.stdin.readline().split())
positions = list(map(int, sys.stdin.readline().split()))
def sol(N, L, positions):
    positions.sort()
    end_pos = 0
    cnt = 0
    for position in positions:
        if position > end_pos:
            cnt += 1
            end_pos = position + L - 1
    return cnt
print(sol(N=N, L=L, positions=positions))
            
        