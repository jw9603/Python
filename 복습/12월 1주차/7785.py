# 7785. 회사에 있는 사람
# https://www.acmicpc.net/problem/7785

import sys
n = int(sys.stdin.readline().strip())
logging = {}
for _ in range(n):
    name, log = sys.stdin.readline().split()
    
    if log == 'enter':
        logging[name] = 1
    else:
        logging[name] = 0
print('\n'.join(sorted([i for i in logging if logging[i] == 1 ],reverse=True)))