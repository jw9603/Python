# 백준 2231. 분해합
# https://www.acmicpc.net/problem/2231
import sys
N = int(sys.stdin.readline().strip())
def generator(N):
    for i in range(1, N + 1):
        res = sum(list(map(int, str(i)))) + i
        
        if res == N:
            print(i)
            return
        if i == N:
            print(0)
            return
generator(N=N)
            
        