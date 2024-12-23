# 백준 16953. A -> B
# https://www.acmicpc.net/problem/16953
import sys
A, B = map(int, sys.stdin.readline().split())

def sol(a, b):
    cnt = 0
    while b > a:
        cnt += 1
        if b % 10 == 1:
            b //= 10
        elif b % 2 == 0:
            b //= 2
        else:
            return -1
    return cnt + 1 if b == a else -1
print(sol(a=A, b=B))