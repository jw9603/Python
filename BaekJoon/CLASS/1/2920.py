# 백준 2920. 음계
# https://www.acmicpc.net/problem/2920
import sys
arr = list(map(int, sys.stdion.readline().split()))
if arr == sorted(arr):
    print('ascending')
elif arr == sorted(arr, reverse=True):
    print('descending')
else:
    print('mixed')