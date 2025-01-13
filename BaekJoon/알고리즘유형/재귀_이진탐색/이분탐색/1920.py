# 백준 1920. 수 찾기
# https://www.acmicpc.net/problem/1920
import sys
from bisect import *
N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
M = list(map(int, sys.stdin.readline().split()))
def idx(arr, target):
    index = bisect_left(arr, target)
    if index != len(arr) and arr[index] == target:
        return index
    else:
        return -1
result = []
A.sort()
for m in M:
    if idx(A, m) != -1:
        result.append(1)
    else:
        result.append(0)
print(*result, sep='\n')

