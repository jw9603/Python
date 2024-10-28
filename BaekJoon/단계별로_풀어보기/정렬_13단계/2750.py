# 2750 - 수 정렬하기
# https://www.acmicpc.net/problem/2750

import sys

def sol(n_list):
    
    n_list.sort()
    
    for i in n_list:
        print(i)
        
N = int(sys.stdin.readline().strip())
n_list = []
for _ in range(N):
    n_list.append(int(sys.stdin.readline().strip()))

sol(n_list)
    
    