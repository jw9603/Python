# 1934. 최소공배수
# https://www.acmicpc.net/problem/1934

import sys
import math
T = int(sys.stdin.readline().strip())

def sol(a, b):
    return a * b // math.gcd(a,b)

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(sol(a=a, b=b))
    