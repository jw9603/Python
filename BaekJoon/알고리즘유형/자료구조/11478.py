# 백준 11478. 서로 다른 부분 문자열의 개수
# https://www.acmicpc.net/problem/11478
import sys
S = sys.stdin.readline().strip()
def sol(s):
    result = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            result.add(s[i:j+1])
    return len(result)
print(sol(s=S))
            