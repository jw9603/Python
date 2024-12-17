# 13241. 최소공배수
# https://www.acmicpc.net/problem/13241

import sys
from math import gcd
a, b = map(int, sys.stdin.readline().split())
def sol(A, B):
    return (A * B) // gcd(A, B)
print(sol(A=a, B=b))