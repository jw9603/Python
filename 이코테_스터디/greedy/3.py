# 이코테 그리디 - 1이 될 때 까지
# import sys

# N, K = map(int,sys.stdin.readline().split())

# result = 0

# while 1:
    
#     while N % K != 0:
#         N -= 1
#         result += 1
        
#     N //= K
#     result += 1
    
#     if N == 1:
#         break
    
# print(result)


###### 좀 더 효율적인 풀이 (O(log_kN))######
import sys

N, K = map(int,sys.stdin.readline().split())

result = 0

while 1:
    
    target = (N // K) * K
    result += (N-target)
    
    N = target
    
    if N < K:
        break
    
    N //= K
    result += 1
result += (N-1)    
print(result)
###### 좀 더 효율적인 풀이 (O(log_kN))######
