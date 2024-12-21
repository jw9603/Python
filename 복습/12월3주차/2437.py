# 백준 2437. 저울
# https://www.acmicpc.net/problem/2437
import sys
N = int(sys.stdin.readline().strip())
weights = sorted(list(map(int, sys.stdin.readline().split())))
total = 1
for w in weights:
    if total < w:
        break
    total += w
print(total)