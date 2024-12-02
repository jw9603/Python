# 11399. ATM
# https://www.acmicpc.net/problem/11399

import sys

N = int(sys.stdin.readline().strip())
time = list(map(int,sys.stdin.readline().split()))
def sol(time):
    time.sort()

    result = 0
    curr = 0
    for i in time:
        
        curr += i
        result += curr
    return result

print(sol(time=time))
    