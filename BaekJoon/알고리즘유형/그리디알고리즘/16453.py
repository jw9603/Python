# 백준 16453. 스테이크버드
# https://www.acmicpc.net/problem/16435
import sys
N, L = map(int, sys.stdin.readline().split())
heights = list(map(int, sys.stdin.readline().split()))
def sol(L, heights):
    heights.sort()
    for height in heights:
        if L >= height:
            L += 1
    print(L)
sol(L=L, heights=heights)