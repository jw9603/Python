# 백준 1264. 모음의 개수
# https://www.acmicpc.net/problem/1264
import sys
while True:
    s = sys.stdin.readline().strip()
    if s == '#':
        break
    cnt = 0
    for i in s:
        if i in 'aeiouAEIOU':
            cnt += 1
    print(cnt)