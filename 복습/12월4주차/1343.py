# 1343. 폴리오미노
# https://www.acmicpc.net/problem/1343
import sys
board = sys.stdin.readline().strip()
board = board.replace('XXXX', 'AAAA').replace('XX', 'BB')
print(board if 'X' not in board else -1)