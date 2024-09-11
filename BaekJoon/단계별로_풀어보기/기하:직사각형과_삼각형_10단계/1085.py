# 직사각혀에서 탈출 - 1085
# https://www.acmicpc.net/problem/1085

import sys

x, y, w, h = map(int,sys.stdin.readline().split())
print(min(abs(x-w),abs(x-0),abs(y-0),abs(y-h)))