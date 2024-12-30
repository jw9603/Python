# 백준 2847. 게임을 만든 동준이
# https://www.acmicpc.net/problem/2847
import sys
N = int(sys.stdin.readline().strip())
scores = [int(sys.stdin.readline().strip()) for _ in range(N)]
def sol(N, scores):
    cnt = 0
    for i in range(N-1, 0, -1):
        if scores[i] <= scores[i - 1]:
            cnt += (scores[i - 1] - scores[i]) + 1
            scores[i - 1] = scores[i] - 1
    return cnt
print(sol(N=N, scores=scores))