# 2869 - 달팽이는 올라가고 싶다.
# https://www.acmicpc.net/problem/2869
import sys

A, B, V = map(int, sys.stdin.readline().split())

if (V-B) % (A-B) == 0:
    print((V-B) // (A-B))
else:
    print((V-B) // (A-B)+1)
    