# 백준 17298. 오큰수
# https://www.acmicpc.net/problem/17298
import sys
N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))
def sol(N, A):
    NGE = [-1] * N
    stack = [0]
    for i in range(1, N):
        while stack and A[stack[-1]] < A[i]:
            NGE[stack.pop()] = A[i]
        stack.append(i)
    print(' '.join(map(str, NGE)))
sol(N=N, A=A)