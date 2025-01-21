# 백준 2470. 두 용액
# https://www.acmicpc.net/problem/2470


############################ 이분 탐색 풀이 ##############################
import sys
N = int(sys.stdin.readline().strip())
values = list(map(int, sys.stdin.readline().split()))

def sol(N, values):
    
    values.sort()
    
    closest_sum = float('inf')
    result = (0, 0)
    
    for i in range(N):
        target = -values[i]
        left, right = i + 1, N - 1
        
        while left <= right:
            mid = (left + right) // 2
            current_sum = values[i] + values[mid]
            
            if abs(current_sum) < abs(closest_sum):
                closest_sum = current_sum
                result = (values[i], values[mid])
            
            if values[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    return tuple(sorted(result))
print(*sol(N=N, values=values))
############################ 이분 탐색 풀이 ##############################

############################ 투 포인터 풀이 ##############################
import sys
N = int(sys.stdin.readline().strip())
values = list(map(int, sys.stdin.readline().split()))

def sol(N, values):
    
    values.sort()
    
    left, right = 0, N - 1
    closest_sum = float('inf')
    result = (0, 0)
    
    while left < right:
        current_sum = values[left] + values[right]
        
        if abs(current_sum) < abs(closest_sum):
            closest_sum = current_sum
            result = (values[left], values[right])
        
        if current_sum < 0:
            left += 1
        elif current_sum > 0:
            right -= 1
        else:
            return result
    return result
print(*sol(N=N, values=values))
############################ 투 포인터 풀이 ##############################
    
            
        