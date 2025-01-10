# 백준 1629. 곱셈
# https://www.acmicpc.net/problem/1629
import sys
a, b, c = map(int, sys.stdin.readline().split())

def sol(a, b, c):
    
    # 1. base case
    if b == 0:
        return 1
    
    # 2. 재귀 호출
    half = sol(a, b // 2, c)
    
    # 3. 데이터 통합
    half = (half * half) % c
    if b % 2 != 0:
        half = (a * half) % c
    return half
print(sol(a=a, b=b, c=c))