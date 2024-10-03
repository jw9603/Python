# 1018 - 체스판 다시 칠하기
# https://www.acmicpc.net/problem/1018

import sys

# N은 가로 개수, M은 세로 개수
N, M = map(int,sys.stdin.readline().split())

chess = []

for _ in range(N):
    chess.append(sys.stdin.readline().strip())

res = []

for a in range(N-7):
    for b in range(M-7):
        white = 0
        black = 0
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i+j) % 2 == 0:
                    if chess[i][j]!= 'W':
                        white += 1
                    else:
                        black += 1
                else:
                    if chess[i][j]!= 'W':
                        black += 1
                    else:
                        white += 1
        res.append(white)
        res.append(black)

print(min(res))