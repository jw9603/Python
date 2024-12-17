# 1934. 최소공배수
# https://www.acmicpc.net/problem/1934
import sys
from math import gcd
T = int(sys.stdin.readline().strip())
def sol(A, B):
    return (A * B) // gcd(A, B)
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(sol(A=a, B=b))
    