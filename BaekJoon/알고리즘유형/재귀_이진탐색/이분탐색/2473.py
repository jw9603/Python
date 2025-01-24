# 백준 2473. 세 용액
# https://www.acmicpc.net/problem/2473
################################ 투 포인터 #################################
import sys
N = int(sys.stdin.readline().strip())
values = list(map(int, sys.stdin.readline().split()))

def sol(N, values):
    values.sort()
    
    closest_sum = float('inf')
    result = (0, 0, 0)
    
    for i in range(N - 2):
        left, right = i + 1, N - 1
        
        while left < right:
            current_sum = values[i] + values[left] + values[right]
            
            if abs(current_sum) < abs(closest_sum):
                closest_sum = current_sum
                result = (values[i], values[left], values[right])
            
            if current_sum < 0:
                left += 1
            elif current_sum > 0:
                right -= 1
            else:
                return sorted(result)
    return sorted(result)
print(*sol(N=N, values=values))
################################ 투 포인터 #################################

################################ 이분 탐색 (시간 초과)#################################
import sys
from bisect import bisect_left
N = int(sys.stdin.readline().strip())
values = list(map(int, sys.stdin.readline().split()))

def sol(N, values):
    values.sort()
    
    closest_sum = float('inf')
    result = (0, 0, 0)
    
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            partial_sum = values[i] + values[j] # 두 값의 합
            target = -partial_sum
            
            idx = bisect_left(values, target, j + 1)
            
            if idx < N and values[idx] == target:
                current_sum = partial_sum + values[idx]
                if abs(current_sum) < abs(closest_sum):
                    closest_sum = current_sum
                    result = (values[i], values[j], values[idx])
                continue
            
            for k in [idx - 1, idx]:
                if k > j and k < N:
                    current_sum = partial_sum + values[k]
                    if abs(current_sum) < abs(closest_sum):
                        closest_sum = current_sum
                        result = (values[i], values[j], values[k])
    return sorted(result)
print(*sol(N=N, values=values))
                    
################################ 이분 탐색 (시간 초과)#################################