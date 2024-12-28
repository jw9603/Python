# 백준 10709. 기상캐스터
# https://www.acmicpc.net/problem/10709
import sys
H, W = map(int, sys.stdin.readline().split())
state = [sys.stdin.readline().strip() for _ in range(H)]
def sol(W, state):
    for s in state:
        sky = [-1] * len(s)
        for w in range(W):
            if s[w] == 'c':
                sky[w] = 0
        for i in range(1, W):
            if sky[i] == -1 and sky[i - 1] != -1:
                sky[i] = sky[i - 1] + 1
        print(*sky)
sol(W=W, state=state)
        