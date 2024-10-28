# 커트라인 - 브론즈 2단계
# https://www.acmicpc.net/problem/25305

import sys

N, k = map(int,sys.stdin.readline().split())

score = list(map(int,sys.stdin.readline().split()))

print(sorted(score,reverse=True)[k-1])