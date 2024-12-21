# 백준 1931. 회의실 배정
# https://www.acmicpc.net/problem/1931
import sys
N = int(sys.stdin.readline().strip())
meetings = sorted([[*map(int, sys.stdin.readline().split())] for _ in range(N)],key=lambda x:(x[1],x[0]))

def sol(meetings):
    cnt = 0
    end_idx = 0
    for i, j in meetings:
        if end_idx <= i:
            cnt += 1
            end_idx = j
    print(cnt)
sol(meetings=meetings)