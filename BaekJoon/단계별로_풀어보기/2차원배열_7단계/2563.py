# 색종이 - 2563번
# https://www.acmicpc.net/problem/2563

import sys

N = int(sys.stdin.readline().strip())

arr = [[0]*100 for _ in range(100)]

# print(arr)

for _ in range(N):
    
    x, y = map(int,sys.stdin.readline().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            arr[i][j] = 1

print(sum(arr[i][j] for i in range(0,100) for j in range(0,100))) 