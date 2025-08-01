# 백준 1018. 체스판 다시 칠하기
# https://www.acmicpc.net/problem/1018
####################################### 문제 이해 #######################################
# 지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 MxN 크기의 보드를 찾았다.
# 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다.
# 지민이는 이 보드를 잘라서 8x8 크기의 체스판으로 만들려고 한다.
# 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다.
# 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다.

# 보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8x8 크기의 체스판으로 잘라낸 후 몇 개의 정사각형을 다시 칠해야
# 겠다고 생각했다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램

# 입력: 첫째 줄에 N과 M이 주어진다. B는 검, W는 흰
# 출력: 첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력

# 알고리즘:
# 1. 입력으로 주어진 MxN 보드에서 8x8 크기의 모든 부분 보드를 확인한다.
# 2. 각 부분 보드에 대해 두 가지 체스판 패턴(검정색 시작, 흰색 시작)을 고려하여
#    다시 칠해야 하는 정사각형의 개수를 계산한다.
# 3. 모든 부분 보드에 대해 다시 칠해야 하는 정사각형의 개수를 비교하여 최솟값을 찾는다.
# 4. 최솟값을 출력한다. 
####################################### 문제 이해 #######################################
def count_paint(board, x, y):
    w, b = 0, 0
    
    for i in range(8):
        for j in range(8):
            expected_w = 'W' if (i + j) % 2 == 0 else 'B'
            excepted_b = 'B' if (i + j) % 2 == 0 else 'W'
            if board[x + i][y + j] != expected_w:
                w += 1
            if board[x + i][y + j] != excepted_b:
                b += 1  
    
    return min(w, b)

def min_paint(N, M, board):
    min_cnt = float('inf')

    for i in range(N - 7):
        for j in range(M - 7):
            min_cnt = min(min_cnt, count_paint(board, i, j))
    
    return min_cnt

def main():
    N, M = map(int, input().split())
    board = [input().strip() for _ in range(N)]
    print(min_paint(N, M, board))

if __name__ == "__main__":
    main()