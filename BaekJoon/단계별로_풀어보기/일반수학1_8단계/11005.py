# 11005 진법 변환2
# https://www.acmicpc.net/problem/11005

import sys
from collections import deque

def jinbub(N,B):
    
    string = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answer = deque()

    while N != 0:
        answer.appendleft(string[N % B])
        N //= B
    return ''.join(answer)
    
N, B = map(int,(sys.stdin.readline().split()))

print(jinbub(N,B))
