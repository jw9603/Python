# 백준 2805. 나무 자르기
# https://www.acmicpc.net/problem/2805
import sys
N, M = map(int, sys.stdin.readline().split())
heights = list(map(int, sys.stdin.readline().split()))
def sol(M, heights):
    low, high = 1, max(heights)
    result = 0
    
    while low <= high:
        mid = (low + high) // 2
        count = sum(max(0, height - mid) for height in heights)
        
        if count >= M:
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result
print(sol(M=M, heights=heights))