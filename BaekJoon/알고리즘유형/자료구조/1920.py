# 백준 1920.수 찾기
# https://www.acmicpc.net/problem/1920

#################### 해쉬 풀이: O(N + M) ####################
import sys
N = int(sys.stdin.readline().strip())
A = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))

def sol(nums, A):
    for num in nums:
        if num in A:
            print(1)
        else:
            print(0)
sol(nums=nums, A=A)
##################### 해쉬 풀이 ####################

#################### 이분 탐색 풀이: O((N+M)logN)  ####################
import sys
from bisect import bisect_left
N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split())) 
M = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))
def idx(arr, target):
    index = bisect_left(arr, target)
    if index != len(arr) and arr[index] == target:
        return index
    else:
        return -1

def sol(nums, A):
    A.sort() # O(NlogN)
    for num in nums: # O(MlogN)
        if idx(A, num) != -1:
            print(1)
        else:
            print(0)
sol(nums=nums, A=A)
#################### 이분 탐색 풀이 ####################