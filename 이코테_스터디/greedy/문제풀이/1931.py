# 1931. 회의실 배정
# https://www.acmicpc.net/problem/1931

import sys

N = int(sys.stdin.readline().strip())
time = []

for _ in range(N):
    s, e = map(int,sys.stdin.readline().split())
    time.append((s, e))

def sol(time):
    time.sort(key=lambda x: (x[1], x[0]))
    
    result, end = 0, 0
    for i, j in time:
        if end <= i:
            result += 1
            end = j
    return result
print(sol(time=time))
    
