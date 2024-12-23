# 백준 1439. 뒤집기
# https://www.acmicpc.net/problem/1439
import sys
S = sys.stdin.readline().strip()
def sol(s):
    cnt = 0
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            cnt += 1
    return (cnt + 1) // 2
print(sol(s=S))