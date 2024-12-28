# 백준 16953. A -> B
# https://www.acmicpc.net/problem/16953
import sys
A, B = map(int, sys.stdin.readline().split())
def sol(A, B):
    cnt = 0
    while B > A:
        cnt += 1
        if B % 10 == 1:
            B //= 10
        elif B % 2 == 0:
            B //= 2
        else:
            return -1
    return cnt + 1 if B == A else -1
print(sol(A=A, B=B))
    