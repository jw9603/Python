# 백준 12904. A와 B
# https://www.acmicpc.net/problem/12904
import sys
S = list(sys.stdin.readline().strip())
T = list(sys.stdin.readline().strip())
def sol(s, t):
    flag = False
    while t:
        
        if t[-1] == 'A':
            t.pop()
        elif t[-1] == 'B':
            t.pop()
            t.reverse()
        if s == t:
            flag = True
            break
    return 1 if flag else 0
print(sol(s=S, t=T))