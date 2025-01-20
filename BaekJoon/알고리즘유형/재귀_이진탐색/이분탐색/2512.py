# 백준 2512. 예산
# https://www.acmicpc.net/problem/2512
import sys
N = int(sys.stdin.readline().strip())
requests = list(map(int, sys.stdin.readline().split())) # N개
total_budget = int(sys.stdin.readline().strip())

def sol(requests, total_budget):
    
    low, high = 0, max(requests)
    result = 0
    
    while low <= high:
        mid = (low + high) // 2
        allocated = 0
        for req in requests:
            allocated += min(req, mid)
        if allocated <= total_budget:
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result
print(sol(requests=requests, total_budget=total_budget))
            