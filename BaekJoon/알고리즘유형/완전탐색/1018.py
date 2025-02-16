# 백준 1018. 체스판 다시 칠하기
# https://www.acmicpc.net/problem/1018
import sys
N, M = map(int, sys.stdin.readline().split())
boards = [list(sys.stdin.readline().strip()) for _ in range(N)]


def count_repairs(boards, x, y):
    w, b = 0, 0 # 'W'로 시작하는 경우와 'B'로 시작하는 경우 각각 다시 칠해야 하는 개수
    for i in range(8):
        for j in range(8):
            expected_w = 'W' if (i + j) % 2 == 0 else 'B'
            expected_b = 'B' if (i + j) % 2 == 0 else 'W'
            
            if boards[x + i][y + j] != expected_w:
                w += 1
            if boards[x +i][y + j] != expected_b:
                b += 1
        
    return min(w, b)

def sol(N, M, boards):
    min_cnt = float('inf')
    for i in range(N - 7):
        for j in range(M - 7):
            min_cnt = min(min_cnt, count_repairs(boards, i, j))
    return min_cnt

print(sol(N=N, M=M, boards=boards))
            