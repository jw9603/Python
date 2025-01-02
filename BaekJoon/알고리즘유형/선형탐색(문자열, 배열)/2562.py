# 백준 2562. 최댓값
# https://www.acmicpc.net/problem/2562
import sys
arr = [int(sys.stdin.readline().strip()) for _ in range(9)]
print(max(arr),arr.index(max(arr)) + 1,sep='\n')