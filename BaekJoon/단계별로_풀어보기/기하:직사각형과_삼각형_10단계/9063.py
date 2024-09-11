# 9063 대지
# https://www.acmicpc.net/problem/9063

import sys

def solution(w,h):
    return (max(w)-min(w))*(max(h)-min(h))
   
N = int(sys.stdin.readline().strip())

w = []
h = []

for _ in range(N):
    x,y = map(int,sys.stdin.readline().split())
    w.append(x)
    h.append(y)

print(solution(w,h))