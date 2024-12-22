# 백준 8958. OX퀴즈
# https://www.acmicpc.net/problem/8958
import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    case = sys.stdin.readline().strip()
    score = 0
    total = 0
    for i in case:
        if i == 'O':
            score += 1
            total += score
        else:
            score = 0
    print(total)