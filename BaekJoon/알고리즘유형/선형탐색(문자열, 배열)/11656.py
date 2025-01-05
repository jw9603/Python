# 백준 11656. 접미사 배열
# https://www.acmicpc.net/problem/11656
import sys
S = sys.stdin.readline().strip()
def sol(s):
    return '\n'.join(sorted([s[i:] for i in range(len(s))]))
print(sol(s=S))
