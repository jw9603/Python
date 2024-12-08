# 백준 10815. 숫자 카드
# https://www.acmicpc.net/problem/10815

import sys

N = int(sys.stdin.readline().strip())
card = set(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
num = list(map(int,sys.stdin.readline().split()))

print(' '.join(['1' if i in card else '0' for i in num]))