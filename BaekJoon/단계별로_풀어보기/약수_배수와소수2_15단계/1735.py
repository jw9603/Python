# 1735. 분수 합
# https://www.acmicpc.net/problem/1735

import sys
from math import gcd
a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())

def sol(a, b, c, d):
    mom = a * d + c * b
    child = b * d
    return (mom // gcd(mom, child)), (child // gcd(mom, child))

result1, result2 = sol(a=a, b=b, c=c, d=d)
print(result1, result2)

