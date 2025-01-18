# 백준 19637. IF문 좀 대신 써줘
# https://www.acmicpc.net/problem/19637
############################# bisect #########################################
import sys
from bisect import bisect_left
N, M = map(int, sys.stdin.readline().split())
title = []
power = []
for _ in range(N):
    a, b = sys.stdin.readline().split()
    title.append(a)
    power.append(int(b))

for _ in range(M):
    print(title[bisect_left(power, int(sys.stdin.readline().strip()))])
############################# bisect #########################################
import sys
N, M = map(int, sys.stdin.readline().split())
title = []
power = []
for _ in range(N):
    a, b = sys.stdin.readline().split()
    title.append(a)
    power.append(int(b))

def binary_search(power, value):
    left, right = 0, len(power) - 1
    while left <= right:
        mid = (left + right) // 2
        if value <= power[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return left
for _ in range(M):
    print(title[binary_search(power, int(sys.stdin.readline().strip()))])
