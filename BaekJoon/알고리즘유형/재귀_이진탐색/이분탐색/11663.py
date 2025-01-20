# 백준 11663. 선분 위의 점
# https://www.acmicpc.net/problem/11663
import sys
from bisect import bisect_left, bisect_right
N, M = map(int, sys.stdin.readline().split())
points = list(map(int, sys.stdin.readline().split()))
segments = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

def sol(segments, points):

    points.sort() # O(NlogN)
    result = []
    
    for l, r in segments: # O(MlogN)
        left_idx = bisect_left(points, l)
        right_idx = bisect_right(points, r)
        result.append(right_idx - left_idx)
    
    return '\n'.join(map(str, result))
print(sol(segments=segments, points=points))