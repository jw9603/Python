# 백준 1026. 보물
# https://www.acmicpc.net/problem/1026
import sys
N = int(sys.stdin.readline().strip())
A = sorted(list(map(int, sys.stdin.readline().split())))
B = sorted(list(map(int, sys.stdin.readline().split())),reverse=True)
def sol(N, A, B): # O(NlogN)
    result = 0
    for i in range(N):
        result += A[i] * B[i]
    print(result)
sol(N=N, A=A, B=B)        
    