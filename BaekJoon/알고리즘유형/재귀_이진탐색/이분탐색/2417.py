# 백준 2417. 정수 제곱근
# https://www.acmicpc.net/problem/2417
import sys
n = int(sys.stdin.readline().strip())
def sol(n):
    low, high = 0, n
    while low <= high:
        mid = (low + high) // 2
        
        if mid ** 2 < n:
            low = mid + 1
        else:
            high = mid - 1
    return low
print(sol(n=n))