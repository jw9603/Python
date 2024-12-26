# 백준 14916. 거스름돈
# https://www.acmicpc.net/problem/14916
import sys
n = int(sys.stdin.readline().strip())
def sol(n):
    cnt = 0
    while n >= 0:
        if n % 5 == 0:
            cnt += n // 5
            return cnt
        else:
            n -= 2
            cnt += 1
    return -1
print(sol(n=n))