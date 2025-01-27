# 백준 1300. K번째 수
# https://www.acmicpc.net/problem/1300
import sys
N = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())

def count(mid, N):
    cnt = 0
    for i in range(1, N + 1):
        if mid // i > N:
            cnt += N
        else:
            cnt += mid // i
    return cnt

def sol(N, k):
    left, right = 1, N * N
    result = 0
    
    while left <= right:
        mid = (left + right) // 2 # mid는 배열 B에서의 인덱스(k)
        
        if count(mid, N) >= k:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result

print(sol(N=N, k=k))
        