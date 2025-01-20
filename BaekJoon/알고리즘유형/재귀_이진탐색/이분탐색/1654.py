# 백준 1654. 랜선 자르기 - 실버 2단계
# https://www.acmicpc.net/problem/1654
import sys
K, N = map(int, sys.stdin.readline().split())
lengths = [int(sys.stdin.readline().strip()) for _ in range(K)]

def sol(N, lengths):
    low, high = 1, max(lengths)
    reuslt = 0
    while low <= high:
        mid = (low + high) // 2
        count = sum(length // mid for length in lengths)
        
        if count >= N:
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result
print(sol(N=N, lengths=lengths))