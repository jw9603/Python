# 백준 10816. 숫자 카드 2
# https://www.acmicpc.net/problem/10816

################################# 해쉬 풀이 O(N + M)###############################
import sys
N = int(sys.stdin.readline().strip())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))

def sol(cards, nums):
    result = []
    cards_dict = {}
    for card in cards:
        if card in cards_dict:
            cards_dict[card] += 1
        else:
            cards_dict[card] = 1
    for num in nums:
        if num in cards_dict:
            result.append(cards_dict[num])
        else:
            result.append(0)
    
    return result
print(*sol(cards=cards, nums=nums))
################################# 해쉬 풀이 ###############################

################################# 이분 탐색 풀이 O((N+M)logN)###############################
import sys
from bisect import *
N = int(sys.stdin.readline().strip())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))

def sol(arr, target):
    left = bisect_left(arr, target)
    right = bisect_right(arr, target)
    return right - left
cards.sort()
for num in nums:
    print(sol(arr=cards, target=num), end=' ')
################################# 이분 탐색 풀이 ###############################