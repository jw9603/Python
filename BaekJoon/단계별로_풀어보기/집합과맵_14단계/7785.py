# 7785. 회사에 있는 사람
# https://www.acmicpc.net/problem/7785

import sys

N = int(sys.stdin.readline().strip())
google = {}
for _ in range(N):
    name, log = map(str, sys.stdin.readline().split())
    
    if log == 'enter':
        google[name] = 1
    else:
        google[name] = 0
        
print('\n'.join(sorted([i for i in google if google[i] == 1],reverse=True)))