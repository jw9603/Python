# 백준 25501. 재귀의 귀재
# https://www.acmicpc.net/problem/25501
import sys
T = int(sys.stdin.readline().strip())
def sol(s, cnt=1):
    # 1. base case
    if len(s) <= 1:
        return 1, cnt
    
    # 2. 재귀 호출
    if s[0] != s[-1]:
        return 0, cnt
    else:
        cnt += 1
        return sol(s[1:-1], cnt)
for _ in range(T):
    s = sys.stdin.readline().strip()
    print(*sol(s=s))