# 1269. 대칭 차집합
# https://www.acmicpc.net/problem/1269

import sys

num_a, num_b = map(int,sys.stdin.readline().split())

a = set(map(int,sys.stdin.readline().split()))
b = set(map(int,sys.stdin.readline().split()))

def sol(a, b):
    return len(a-b | b-a)
print(sol(a=a, b=b))