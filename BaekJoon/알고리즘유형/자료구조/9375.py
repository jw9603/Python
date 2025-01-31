# 백준 9375. 패션왕 신해빈
# https://www.acmicpc.net/problem/9375
import sys
from collections import defaultdict
T = int(sys.stdin.readline().strip())

for _ in range(T):
    n = int(sys.stdin.readline().strip())
    wears = defaultdict(list)
    for _ in range(n):
        name, type = sys.stdin.readline().split()
        
        if type in wears:
            wears[type].append(name)
        else:
            wears[type] = [name]
    
    cnt = 1
    for i in wears:
        cnt *= (len(wears[i]) + 1)
    print(cnt - 1)
    
    