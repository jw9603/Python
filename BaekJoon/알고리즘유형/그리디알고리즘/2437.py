# 2437. 저울
# https://www.acmicpc.net/problem/2437
import sys
N = int(sys.stdin.readline().strip())
weight = list(map(int, sys.stdin.readline().split()))
def sol(weight):
    weight.sort()
    result = 1
    for w in weight:
        if result < w:
            break
        result += w
    return result
print(sol(weight=weight))