# 1269. 대칭 차집합
# https://www.acmicpc.net/problem/1269

import sys

a, b = map(int,sys.stdin.readline().split())
list_a = set(map(int,sys.stdin.readline().split()))
list_b = set(map(int,sys.stdin.readline().split()))

def sol(list_a, list_b):
    return len(list_a - list_b | list_b - list_a)
print(sol(list_a=list_a, list_b=list_b))