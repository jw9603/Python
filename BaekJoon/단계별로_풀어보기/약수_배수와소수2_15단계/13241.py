# 13241. 최소 공배수
# https://www.acmicpc.net/problem/13241

import sys
import math
def sol(a, b):
    return a * b // math.gcd(a,b)
a, b = map(int, sys.stdin.readline().split())
print(sol(a=a, b=b))