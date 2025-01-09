# 백준 4779. 칸토어 집합
# https://www.acmicpc.net/problem/4779
import sys

def sol(n):
    
    # 1. base case
    if n == 0:
        return '-'
    
    # 2. 재귀 호출
    prev = sol(n - 1)
    space = ' ' * len(prev)
    
    # 3. 데이터 통합
    return ''.join([prev, space, prev])
    pass
while True:
    try:
        n = int(sys.stdin.readline().strip())
        print(sol(n))
    except:
        break