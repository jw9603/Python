# 10610. 30
# https://www.acmicpc.net/problem/10610

import sys

N = sys.stdin.readline().strip()

def sol(N):
    if '0' not in N:
        return -1
    
    num_sum = sum([int(i) for i in N])
    
    if num_sum % 3 != 0:
        return -1
    
    return ''.join(sorted(N,reverse=True))

print(sol(N=N))
    