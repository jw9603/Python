# 19532 - 수학은 비대면강의입니다.
# https://www.acmicpc.net/problem/19532

import sys

a,b,c,d,e,f = map(int,sys.stdin.readline().split())
            
def sol(a,b,c,d,e,f):
    for i in range(-999,1000):
        for j in range(-999,1000):
            if a*i + b*j == c and d * i + e * j == f:
                return i,j

print(sol(a,b,c,d,e,f)[0],sol(a,b,c,d,e,f)[1])
            