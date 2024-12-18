# 1946. 신입 사원
# https://www.acmicpc.net/problem/1946

import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    scores = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    scores.sort()
    
    cnt = 1
    max_score = scores[0][1]
    for i in range(1, N):
        if max_score > scores[i][1]:
            cnt += 1
            max_score = scores[i][1]
    print(cnt)