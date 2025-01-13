# 백준 1789. 수들의 합
# https://www.acmicpc.net/problem/1789
import sys
S = int(sys.stdin.readline().strip())

def sol(S):
    low, high = 1, S
    
    result = 0
    
    while low <= high:
        mid = (low + high) // 2
        
        total = mid * (mid + 1) // 2
        
        if total <= S:
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result
print(sol(S=S))