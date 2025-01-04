# 백준 1522. 문자열 교환
# https://www.acmicpc.net/problem/1522
import sys
s = sys.stdin.readline().strip()
def sol(s):
    a_cnt = s.count('a')
    s += s[:a_cnt - 1]
    min_val = float('inf')
    for i in range(len(s) - (a_cnt - 1)):
        min_val = min(min_val, s[i:i + a_cnt].count('b'))
    return min_val
print(sol(s=s))
        