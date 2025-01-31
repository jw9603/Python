# 백준 7785. 회사에 있는 사람
# https://www.acmicpc.net/problem/7785
import sys
n = int(sys.stdin.readline().strip())
log_dict = {}
for _ in range(n):
    name, log = sys.stdin.readline().split()
    
    if log == 'enter':
        log_dict[name] = 1
    else:
        log_dict[name] = 0
    
print('\n'.join(sorted([i for i in log_dict if log_dict[i] == 1], reverse=True)))