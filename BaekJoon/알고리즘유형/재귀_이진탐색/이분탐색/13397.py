# 백준 13397. 구간 나누기 2
# https://www.acmicpc.net/problem/13397
import sys
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
def segment_cnt(arr, N, M, score):
    
    segments = 1
    current_min, current_max = arr[0], arr[0]
    
    for i in range(1, N):
        current_min = min(current_min, arr[i])
        current_max = max(current_max, arr[i])
        
        # 구간 점수가 score를 넘기는지..
        if current_max - current_min > score:
            segments += 1
            current_min, current_max = arr[i], arr[i]
            
            if segments > M:
                return False
    return True

def sol(N, M, arr):
    left, right = 0, max(arr) - min(arr)
    result = right
    
    while left <= right:
        mid = (left + right) // 2
        
        if segment_cnt(arr, N, M, mid): # segments <= M -> score를 줄이자 -> mid를 줄이자
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result
print(sol(N=N, M=M, arr=arr))