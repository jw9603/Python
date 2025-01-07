# 백준 2609. 최대공약수와 최소공배수
# https://www.acmicpc.net/problem/2609
import sys
a, b = map(int, sys.stdin.readline().split())
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
def lcm(a,b):
    return a * b // gcd(a, b)
print(gcd(a, b), lcm(a,b), sep='\n')
