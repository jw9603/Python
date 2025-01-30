# 백준 10815. 숫자 카드
# https://www.acmicpc.net/problem/10815
########################### 해시 방법 #########################
import sys
N = int(sys.stdin.readline().strip())
cards = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))

def sol(cards, nums):
    
    result = []
    for num in nums:
        if num in cards:
            result.append(1)
        else:
            result.append(0)
    return result
print(*sol(cards=cards, nums=nums))
########################### 해시 방법 #########################

########################### 이분 탐색 방법 #########################
import sys
from bisect import *
N = int(sys.stdin.readline().strip())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))
def idx(arr, target):
    index = bisect_left(arr, target)
    if len(arr) != index and arr[index] == target:
        return 1
    else:
        return 0
def sol(cards, nums):
    cards.sort()
    result = []
    for num in nums:
        if idx(cards, num):
            result.append(1)
        else:
            result.append(0)
    return result
print(*sol(cards=cards, nums=nums))
########################### 이분 탐색 방법 #########################