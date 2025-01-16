# 백준 10816. 숫자 카드 2
# https://www.acmicpc.net/problem/10816
import sys
from bisect import *
N = int(sys.stdin.readline().strip())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
queries = list(map(int, sys.stdin.readline().split()))

cards.sort()
def sol(arr, target):
    left = bisect_left(arr, target)
    right = bisect_right(arr, target)
    return right - left

print(' '.join(map(str, [sol(cards, q) for q in queries])))
