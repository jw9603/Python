# 백준 10815. 숫자 카드
# https://www.acmicpc.net/problem/10815

######################### 이진 탐색 풀이 ############################
import sys
from bisect import *
N = int(sys.stdin.readline().strip())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
m = list(map(int, sys.stdin.readline().split()))
def binary_search(arr, target):
    idx = bisect_left(arr, target)
    if len(arr) != idx and arr[idx] == target:
        return idx
    else:
        return -1

cards.sort()
result = []
for i in m:
    if binary_search(cards, i) != -1:
        result.append(1)
    else:
        result.append(0)
print(*result)
######################### 이진 탐색 풀이 ############################

########################### 해쉬 풀이 ###############################
import sys

N = int(sys.stdin.readline().strip())
card = set(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
num = list(map(int,sys.stdin.readline().split()))

print(' '.join(['1' if i in card else '0' for i in num]))
########################### 해쉬 풀이 ###############################
        