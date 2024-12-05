# 1931. 회의실 배정
# https://www.acmicpc.net/problem/1931

import sys

N = int(sys.stdin.readline().strip())
meeting = []
for _ in range(N):
    a, b = map(int,sys.stdin.readline().split())
    meeting.append((a,b))

def sol(meeting):
    meeting.sort(key=lambda x:(x[1],x[0]))

    mid_end, result = 0, 0
    for i, j in meeting:
        if mid_end <= i:
            result += 1
            mid_end = j
    return result

print(sol(meeting=meeting))