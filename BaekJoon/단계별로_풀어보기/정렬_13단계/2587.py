# 2587 - 대표값2
# https://www.acmicpc.net/problem/2587

import sys

def sol(n_list):
    
    n_list.sort()
    
    print(sum(n_list) // 5,n_list[2],sep='\n')
    
n_list = []
    
for _ in range(5):
    n_list.append(int(sys.stdin.readline().strip()))

sol(n_list)