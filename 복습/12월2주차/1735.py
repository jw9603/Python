# 1735. 분수 합
# https://www.acmicpc.net/problem/1735
import sys
from math import gcd
A, B = map(int, sys.stdin.readline().split())
C, D = map(int, sys.stdin.readline().split())

def sol(a, b, c, d):
    child = a * d + c * b
    mom = b * d
    return ' '.join(map(str, [child // gcd(child, mom), mom // gcd(child, mom)]))
print(sol(a=A, b=B, c=C, d=D))