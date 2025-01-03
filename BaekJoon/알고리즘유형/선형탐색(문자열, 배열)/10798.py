# 백준 10798. 세로읽기
# https://www.acmicpc.net/problem/10798
import sys
words = [sys.stdin.readline().strip() for _ in range(5)]
for i in range(15):
    for j in range(5):
        if i < len(words[j]):
            print(words[j][i], end='')