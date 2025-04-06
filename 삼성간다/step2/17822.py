# 백준 17822. 원판 돌리기
# https://www.acmicpc.net/problem/17822

# 반지름이 1, 2, ..., N인 원판이 크기가 작아지는 순으로 놓여있음. 중심은 같다
# 큰 원판이 밑에, 작은 원판이 위에 있다는 말
# 원판의 반지름이 i이면, 그 원판을 i번째 원판이라고 한다.
# 각각의 원판에는 M개의 정수가 적혀있고,
# i번째 원판에 적힌 j번째 수의 위치는 (i, j)로 표현

# 원판의 회전은 독립적으로 이루어진다.

# 원판을 아래와 같은 방법으로 총 T번 회전시키려고 한다.
# 원판의 횐전 방법은 미리 정해져 있고, i번째 회전할 때 사용하는 변수는 x_i, d_i, k_i이다.

# x_i: 원판의 번호
# d_i: 0 = 시계, 1 = 반시계
# k_i: 몇 칸
from collections import deque
def remove_adjacent(board, N, M):
    removed = False
    visited = [[False] * M for _ in range(N)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    to_removed = set()

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0 or visited[i][j]:
                continue
            queue = deque([(i, j)])
            visited[i][j] = True
            same = [(i, j)]
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, (y + dy) % M
                    if 0 <= nx < N and not visited[nx][ny] and board[nx][ny] == board[x][y]:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        same.append((nx, ny))
            
            if len(same) > 1:
                removed = True
                for x, y in same:
                    to_removed.add((x, y))
    
    for x, y in to_removed:
        board[x][y] = 0
    
    return removed

def adjust_numbers(board, N, M):
    '''
    없는 경우에는 원판에 적힌 수의 평균을 구하고, 
    평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.
    '''
    total = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                total += board[i][j]
                cnt += 1
    if not cnt:
        return
 
    avg = total / cnt
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0: # 0은 원판에 적힌 수가 아님
                continue
            if board[i][j] > avg:
                board[i][j] -= 1
            elif board[i][j] < avg:
                board[i][j] += 1

def rotate(board, x, d, k, N):
    for i in range(x - 1, N, x):
        if d == 0: # 시계
            board[i].rotate(k)
        else:
            board[i].rotate(-k)

def main():
    N, M, T = map(int, input().split())
    board = [deque(map(int, input().split())) for _ in range(N)]
    operations = [tuple(map(int, input().split())) for _ in range(T)]

    for x, d, k in operations:
        rotate(board, x, d, k, N)
        if not remove_adjacent(board, N, M): # 제거할 게 없을 때 아래 실행
            adjust_numbers(board, N, M)
    
    print(sum(map(sum, board)))

if __name__ == '__main__':
    main()