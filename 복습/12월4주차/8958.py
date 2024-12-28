# 백준 8958. OX퀴즈
# https://www.acmicpc.net/problem/8958
import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    case = sys.stdin.readline().strip()
    score = 0
    cnt = 0
    for c in case:
        if c == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)
            