# 1427 - 소트인사이드
# https://www.acmicpc.net/problem/1427

import sys
N = sorted(list(map(int,sys.stdin.readline().strip())),reverse=True)
print(''.join([str(i) for i in N]))
