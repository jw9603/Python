# 백준 1477. 휴게소 세우기
# https://www.acmicpc.net/problem/1477
import sys
import math
N, M, L = map(int, sys.stdin.readline().split())
positions = list(map(int, sys.stdin.readline().split())) if N > 0 else []

def sol(N, M, L, positions):
    positions = [0] + sorted(positions) + [L]
    distances = [positions[i + 1] - positions[i] for i in range(len(positions)- 1)]
    
    left, right = 1, L - 1
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        
        required = 0
        for dist in distances:
            if dist > mid:
                required += math.ceil(dist / mid) - 1
        
        if required <= M:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result
print(sol(N=N, M=M, L=L, positions=positions))
                
            
        
        