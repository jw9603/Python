# 백준 3024. 마라톤 틱택토
# https://www.acmicpc.net/problem/3024
################################## 문제 이해 ##################################
# 5명이 마라톤 틱택토 게임
# N x N 보드에서 진행
# 맨 처음에는 모든 칸은 비어있다. 플레이어는 번갈아?가면서 자신의 영어 이름의 첫글자를 빈 칸에 적는다.
# 게임은 세 글자가 행, 열, 또는 대각선으로 연속할 때, 그 플레이어가 승리하며, 게임 끝
# '.'는 빈 칸을 나타낸다.

################################## 문제 이해 ##################################
def check(N, board): # O(N^2)
 
    for i in range(N):
        for j in range(N):
            if board[i][j] == '.':
                continue

            # 가로
            if j <= N - 3 and board[i][j] == board[i][j + 1] == board[i][j + 2]:
                return board[i][j]
            
            # 세로
            if i <= N - 3 and board[i][j] == board[i + 1][j] == board[i + 2][j]:
                return board[i][j]

            # 우측 아래 대각선
            if i <= N - 3 and j <= N - 3 and board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2]:
                return board[i][j]

            # 좌측 아래 대각선
            if i <= N - 3 and j >= 2 and board[i][j] == board[i + 1][j - 1] == board[i + 2][j - 2]:
                return board[i][j]
    
    return None

def sol(N, board):
    ans = check(N, board)

    if ans:
        print(ans)
    else:
        print('ongoing')


def main():
    N = int(input().strip())
    board = [input().strip() for _ in range(N)]

    sol(N, board)

if __name__ == '__main__':
    main()