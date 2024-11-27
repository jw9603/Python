# 11399. ATM
# https://www.acmicpc.net/problem/11399

import sys

N = int(sys.stdin.readline().strip())
time = sorted(list(map(int,sys.stdin.readline().split())))

def sol(N,time):
    result = 0
    
    for i in range(N):
        for j in range(i+1):
            result += time[j]
    return result
print(sol(N=N,time=time))
