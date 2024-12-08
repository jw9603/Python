# 11478. 서로 다른 부분 문자열의 개수
# https://www.acmicpc.net/problem/11478

import sys

S = sys.stdin.readline().strip()

def sol(S):
    string_set = set()

    for i in range(len(S)):
        for j in range(i, len(S)):
            string_set.add(S[i:j+1])
    return len(string_set)

print(sol(S=S))