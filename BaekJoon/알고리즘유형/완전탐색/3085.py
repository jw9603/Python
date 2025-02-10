# 백준 3085. 사탕 게임
# https://www.acmicpc.net/problem/3085
import sys
N = int(sys.stdin.readline().strip())
boards = [list(sys.stdin.readline().strip()) for _ in range(N)]

def get_max_candy(boards, N):
    max_candy = 1
    for i in range(N):
        row_cnt, col_cnt = 1, 1
        for j in range(1, N):
            # 행 방향 확인
            if boards[i][j] == boards[i][j - 1]:
                row_cnt += 1
            else:
                max_candy = max(max_candy, row_cnt)
                row_cnt = 1
            # 열 방향 확인
            if boards[j][i] == boards[j - 1][i]:
                col_cnt += 1
            else:
                max_candy = max(max_candy, col_cnt)
                col_cnt = 1
        max_candy = max(row_cnt, col_cnt, max_candy)
    return max_candy
                
                

def sol(N, boards):
    
    max_candy = 1
    
    for i in range(N):
        for j in range(N - 1):
            # 오른쪽과 교환
            if boards[i][j] != boards[i][j + 1]:
                boards[i][j], boards[i][j + 1] = boards[i][j + 1], boards[i][j]
                max_candy = max(max_candy, get_max_candy(boards, N))
                boards[i][j], boards[i][j + 1] = boards[i][j + 1], boards[i][j]
            # 아래쪽과 교환
            if boards[j][i] != boards[j + 1][i]:
                boards[j][i], boards[j + 1][i] = boards[j + 1][i], boards[j][i]
                max_candy = max(max_candy, get_max_candy(boards, N))
                boards[j][i], boards[j + 1][i] = boards[j + 1][i], boards[j][i]
    return max_candy

print(sol(N=N, boards=boards))