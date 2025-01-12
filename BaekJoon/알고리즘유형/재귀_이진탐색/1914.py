# 백준 1914. 하노이 탑
# https://www.acmicpc.net/problem/1914
import sys
N = int(sys.stdin.readline().strip())

def sol(N, start, end, mid):
    
    # 1. base case
    if N == 1:
        print(start, end)
        return
    
    # 2. 재귀 호출
    sol(N - 1, start, mid, end)
    
    print(start, end)
    
    sol(N - 1, mid, end, start)
if N > 20:
    print(2 ** N - 1)
else:
    print(2 ** N - 1)
    sol(N, 1, 3, 2)