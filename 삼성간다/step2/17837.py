# 백준 17837. 새로운 게임 2
# https://www.acmicpc.net/problem/17837

# 사용하는 말의 개수: K개,
# 하나의 말 위에 다른 말을 올릴 수 있다.
# 체스판의 각 칸은 흰색, 빨간색, 파란색 중 하나로 색칠되어있다.

# 게임은 체스판 위에 말 K개를 놓고 시작한다. 
# 말은 1~K번, 상/하/좌/우 이동 가능

# Turn 1번은 1번 말부터 K번 말까지 순서대로 이동시키는 것
# 턴이 진행되던 중에 말이 4개 이상 쌓이는 순간 게임 종료

# A번 말이 이동하려는 칸이 흰색(0), 빨간색(1), 파란색(2)
# 흰색(0): 그대로 쌓기 -> 기존에 있는 리스트. extend([말 리스트])
# 빨간색(1): 쌓은후 순서 뒤집기 -> reversed([]) 하지만 말만 뒤집는 것
# 파란색(2): 방향 반대로 바꿔 한 칸 다시 이동 시도, 파란색이면 이동 못함

# 종료 조건: 한 칸에 말이 4개 이상 쌓이는 순간
# 방향 (정지, 우, 좌, 상, 하)
# dx = [0, 0, 0, -1, 1]
# dy = [0, 1, -1, 0, 0]
# reversed_dir = [0, 2, 1, 4, 3]
def move_piece(board, horses, board_map, idx, N):
    '''
    move_piece는 idx 말을 진행하는 함수
    '''
    global dx, dy, reversed_dir

    x, y, d = horses[idx] # idx번째 말

    nx, ny = x + dx[d], y + dy[d]

    # 현재 칸에서 해당 말부터 위에 쌓여 있는 말들 확인 및 추출
    pos = board_map[x][y].index(idx)
    moving_stack = board_map[x][y][pos:]
    board_map[x][y] = board_map[x][y][:pos]

    # 파란색 or 체스판 벗어남
    if not (0 <= nx < N and 0 <= ny < N) or board[nx][ny] == 2:
        
        d = reversed_dir[d]
        horses[idx][2] = d

        nx, ny = x + dx[d], y + dy[d]
        # 방향을 반대로 바꾼 후에 이동하려는 칸이 파란색인 경우에는 이동하지 않고 가만히 있는다.
        if not (0 <= nx < N and 0 <= ny < N) or board[nx][ny] == 2:
            board_map[x][y].extend(moving_stack)
            return False
    
    # 흰, 빨: 이동
    if board[nx][ny] == 0:   # 흰
        board_map[nx][ny].extend(moving_stack)
    elif board[nx][ny] == 1: # 빨
        board_map[nx][ny].extend(reversed(moving_stack))
    
    for horse in moving_stack:
        horses[horse][0] = nx
        horses[horse][1] = ny
    
    if len(board_map[nx][ny]) >= 4:
        return True

    return False
    
def simulate(N, K, board, horses):
    # 체스판에 쌓인 말 정보
    board_map = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(K):
        x, y, d = horses[i]
        board_map[x][y].append(i)
    
    for turn in range(1, 1001): # 1 turn씩 진행
        for i in range(K):      # 모든 말 이동 진행, 즉, move_piece는 하나의 말을 진행하는 함수
            if move_piece(board, horses, board_map, i, N):
                return turn
    return -1

def main():
    global dx, dy, reversed_dir

    # N: 체스판 크기, K: 말의 개수
    N, K = map(int, input().split())

    # 0: 흰색, 1: 빨간색, 2: 파란색
    board = [list(map(int, input().split())) for _ in range(N)]

    # (행, 열, 이동 방향), 행과 열의 번호는 1부터 시작
    horses = []
    for _ in range(K):
        x, y, d = map(int, input().split())
        horses.append([x - 1, y - 1, d])

    dx = [0, 0, 0, -1, 1]
    dy = [0, 1, -1, 0, 0]
    reversed_dir = [0, 2, 1, 4, 3]

    print(simulate(N, K, board, horses))

if __name__ == '__main__':
    main()