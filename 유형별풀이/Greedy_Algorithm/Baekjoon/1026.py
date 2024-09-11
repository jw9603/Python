# 1026 - 보물
# https://www.acmicpc.net/problem/1026

import sys

def sol(N,A,B):
    
    result = 0

    for i in range(N):
        
        result += min(A) * max(B)
        
        A.pop(A.index(min(A)))
        B.pop(B.index(max(B)))
        
    return result

N = int(sys.stdin.readline().strip())
A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))

    
print(sol(N,A,B))


################# 미리 정렬하기 #################
import sys

def sol(N,A,B):
    A.sort()
    B.sort(reverse=True)
    
    result = 0
    for i in range(N):
        result += A[i] * B[i]
    return result

N = int(sys.stdin.readline().strip())
A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))

    
print(sol(N,A,B))
################# 미리 정렬하기 #################
