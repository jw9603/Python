# 백준 1789. 수들의 합
# https://www.acmicpc.net/problem/1789
import sys
from math import sqrt
S = int(sys.stdin.readline().strip())
print(int((-1 + sqrt(1 + 8 * S))// 2))