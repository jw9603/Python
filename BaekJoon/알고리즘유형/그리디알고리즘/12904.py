# 백준 12904. A와 B
# https://www.acmicpc.net/problem/12904
import sys
S = sys.stdin.readline().strip()
T = sys.stdin.readline().strip()
flag = False
while T:
    if T[-1] == 'A':
        T = T[:-1]
    elif T[-1] == 'B':
        T = T[:-1]
        T = T[::-1]
    if S == T:
        flag = True
        break
print(1 if flag else 0)
    