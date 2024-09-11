# 14215 - 세 막대
# https://www.acmicpc.net/problem/14215

# 길이가 작은 두변의 합이 제일 긴 변보다 커야 한다.

import sys

tri_len = sorted(list(map(int,sys.stdin.readline().split())))

if tri_len[0] + tri_len[1] > tri_len[2]:
    print(sum(tri_len))
else:
    print(2*(tri_len[0]+tri_len[1])-1)