# 수학적 호기심 9094번
# https://www.acmicpc.net/problem/9094

import sys

def ispair(n,m):
    cnt = 0
    for a in range(1,n):
        for b in range(a+1,n):
            if (a ** 2 + b ** 2 + m) % (a * b) == 0:
                cnt += 1
    return cnt


T = int(sys.stdin.readline().strip())
for _ in range(T):
    n, m = map(int,sys.stdin.readline().split())
    print(ispair(n,m))