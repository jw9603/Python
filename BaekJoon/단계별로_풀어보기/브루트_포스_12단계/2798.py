# 블랙잭 - 2798
# https://www.acmicpc.net/problem/2798

import sys

N, M = map(int,sys.stdin.readline().split())
card = list(map(int,sys.stdin.readline().split()))

def solution(card,M):
    result = 0
    for i in range(len(card)):
        for j in range(i+1,len(card)):
            for k in range(j+1,len(card)):
                if card[i] + card[j] + card[k] > M:
                    continue
                result = max(result,card[i]+card[j]+card[k])
    return result

print(solution(card,M))