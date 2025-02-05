# 백준 17299. 오등큰수
# https://www.acmicpc.net/problem/17299
import sys
from collections import Counter
N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))
def sol(N, A):
    
    result = [-1] * N
    stack = []
    freq = Counter(A)
    
    for i in range(N):
        while stack and freq[A[stack[-1]]] < freq[A[i]]:
            result[stack.pop()] = A[i]
        stack.append(i)
    return result
print(*sol(N=N, A=A))
    