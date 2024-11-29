# 10610. 30
# https://www.acmicpc.net/problem/10610

import sys

N = sys.stdin.readline().strip()

def sol(N):
    num_sum = 0
    
    if '0' not in N:
        return -1
    
    for i in N:
        num_sum += int(i)
    
    if num_sum % 3 != 0:
        return -1
    
    return ''.join(sorted(N,reverse=True))

print(sol(N=N))


    
    
    

