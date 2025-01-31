# 백준 14425. 문자열 집합
# https://www.acmicpc.net/problem/14425
import sys
N, M = map(int, sys.stdin.readline().split())
S = set(sys.stdin.readline().strip() for _ in range(N))
check_string = [sys.stdin.readline().strip() for _ in range(M)]
def sol(S, check_string):
    
    cnt = 0
    for char in check_string:
        if char in S:
            cnt += 1
    return cnt
print(sol(S=S, check_string=check_string))
