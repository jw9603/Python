# 백준 12015. 가장 긴 증가하는 부분 수열 2
# https://www.acmicpc.net/problem/12015
import sys
from bisect import bisect_left
N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))

def sol(arr):
    sub = []
    for num in arr:
        idx = bisect_left(sub, num)
        if idx == len(sub):
            sub.append(num)
        else:
            sub[idx] = num
    return len(sub)
print(sol(arr=A))            