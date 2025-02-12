# 백준 2003. 수들의 합 2
# https://www.acmicpc.net/problem/2003

######################## 투 포인터 #####################
import sys
N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
def sol(A, M):
    start, end = 0, 0
    cnt = 0
    current_sum = 0
    
    while end < N:
    
        current_sum += A[end]
        end += 1
        
        while current_sum > M and start < end:
            current_sum -= A[start]
            start += 1
        if current_sum == M:
            cnt += 1
    return cnt
print(sol(A=A, M=M))
######################## 투 포인터 #####################

######################## 완전 탐색 #####################
import sys
N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

def sol(A, M):
    cnt = 0
    for i in range(N):
        current_sum = 0
        for j in range(i, N):
            current_sum += A[j]
            if current_sum == M:
                cnt += 1
    return cnt
print(sol(A=A, M=M))         
######################## 완전 탐색 #####################      
            
            