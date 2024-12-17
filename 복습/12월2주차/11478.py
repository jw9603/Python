# 11478. 서로 다른 부분 문자열의 개수
# https://www.acmicpc.net/problem/11478
import sys
S = sys.stdin.readline().strip()
result = set()
for i in range(len(S)):
    for j in range(i,len(S)):
        result.add(S[i:j + 1])
print(len(result))