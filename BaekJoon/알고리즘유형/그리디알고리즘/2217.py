# 백준 2217. 로프
# https://www.acmicpc.net/problem/2217
import sys
N = int(sys.stdin.readline().strip())
rope = sorted([int(sys.stdin.readline().strip()) for _ in range(N)])

def sol(N, rope):
    result = []
    for r in rope:
        result.append(r * N)
        N -= 1
    print(max(result))
sol(N=N, rope=rope)
        
    