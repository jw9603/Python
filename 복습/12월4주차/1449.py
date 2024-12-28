# 백준 1449. 수리공 항승
# https://www.acmicpc.net/problem/1449
import sys
N, L = map(int, sys.stdin.readline().split())
pos = sorted(list(map(int, sys.stdin.readline().split())))

cnt = 0
tmp = 0
for i in pos:
    if i > tmp:
        tmp = i + L - 1
        cnt += 1
print(cnt)