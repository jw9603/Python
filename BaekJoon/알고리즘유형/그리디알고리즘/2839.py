# 백준 2839. 설탕 배달
# https://www.acmicpc.net/problem/2839
import sys
N = int(sys.stdin.readline().strip())
def sol(N):
    cnt = 0
    while N >= 0:
        if N % 5 == 0:
            cnt += N // 5
            return cnt
        else:
            N -= 3
            cnt += 1
    return -1
print(sol(N=N))