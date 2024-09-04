# 1193 - 분수 찾기
# https://www.acmicpc.net/problem/1193
import sys
import math

X = int(sys.stdin.readline().strip())
n = int((math.sqrt(1 + 8 * X)-1) // 2) # 몇번째 줄

if X > n * (n + 1) // 2:
    n += 1
    
# 이제 몇번째 줄인지 알았으니 n의 위치를 알아야 함.
idx = X - (n-1) * n // 2

if n % 2 == 0:
    b = idx
    a = n - idx + 1
    
else:
    b = n - idx + 1
    a = idx
    
print(f"{b}/{a}")