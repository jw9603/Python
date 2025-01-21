# 백준 20444. 색종이와 가위
# https://www.acmicpc.net/problem/20444
import sys
n, k = map(int, sys.stdin.readline().split())
def sol(n, k):
    low, high = 0, n
    
    while low <= high:
        mid = (low + high) // 2
        
        total_cnt = (mid + 1) * (n - mid + 1)
        
        if total_cnt == k:
            print('YES')
            return
        elif total_cnt < k:
            low = mid + 1
        else:
            high = mid - 1
    print('NO')
sol(n=n, k=k)