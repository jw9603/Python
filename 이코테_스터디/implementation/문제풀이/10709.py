# 백준 10709. 기상캐스터
# https://www.acmicpc.net/problem/10709
# 몇 분후에 처음으로 구역에 구름이 뜨는지를 표시한다.
# 처음부터 구역에 구름이 떠있었던 경우에는 0을, 
# 몇분이 지나도 구름이 뜨지 않을 경우에는 -1을 출력한다.
import sys
H, W = map(int, sys.stdin.readline().split())
state = [sys.stdin.readline().strip() for _ in range(H)]

for s in state: # s는 한 줄씩 나옴
    sky = [-1] * len(s)
    for i in range(W):
        if s[i] == 'c':
            sky[i] = 0

    for i in range(1, W):
        if sky[i] == -1 and sky[i - 1] != -1:
            sky[i] = sky[i - 1] + 1
    print(*sky)
            
    