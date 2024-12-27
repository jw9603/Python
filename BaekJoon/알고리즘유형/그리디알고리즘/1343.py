# 백준 1343. 폴리오미노
# https://www.acmicpc.net/problem/1343
import sys
boards = sys.stdin.readline().strip()
boards = boards.replace('XXXX', 'AAAA').replace('XX', 'BB')
print(-1 if 'X' in boards else boards)