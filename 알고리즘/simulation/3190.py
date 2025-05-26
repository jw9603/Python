# 백준 3190. 뱀
# https://www.acmicpc.net/problem/3190
############################### 문제 이해 ###############################
# 뱀이 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.
# 게임은 N * N 보드위에서 진행, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에 벽이 있다.
# 게임이 시작할 때 뱀은 (0,0)에 위치하고 뱀의 길이는 1이다. 처음에 오른쪽을 향한다.

# 뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다:
# 몸길이를 늘려 머리를 다음칸에 위치시킨다.
# 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
# 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
# 만약 이동한 칸에 사과가 없다면, 몸 길이를 줄여서 꼬리가 위치한 칸을 비워준다. (popleft)

# 사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산.

# 입력
# 첫째 줄에 보드의 크기 N과 다음 줄에 사과의 개수 K가 주어진다.
# 다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열
# 사과의 위치는 모두 다르며, 맨위 맨 좌측에는 사과가 없다.(1행 1열) - 1 index 확인
# 다음 줄에는 뱀의 방향 변환 횟수 L

############################### 문제 이해 ###############################
from collections import deque
def count_game_over_time(N, apples, directions):
    # 처음에 오른쪽
    direction = 0

    # 동, 남, 서, 북
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    board = [[0] * N for _ in range(N)]
    for x, y in apples:
        board[x][y] = 1
    
    time = 0

    direction_change = {}
    for t, d in directions:
        direction_change[t] = d
    
    snake = deque([(0, 0)])

    while True:
        time += 1

        head_x, head_y = snake[-1]

        next_x, next_y = head_x + dx[direction], head_y + dy[direction]

        # 벽이나 자기자신의 몸과 부딪힌 경우
        if not(0 <= next_x < N and 0 <= next_y < N) or (next_x, next_y) in snake:
            return time

        snake.append((next_x, next_y))

        # 사과가 있다.
        if board[next_x][next_y] == 1:
            board[next_x][next_y] = 0
        # 사과가 없다.
        else:
            snake.popleft()

        # 방향 변환 
        if time in direction_change:
            turn = direction_change[time]

            if turn == 'L':
                direction = (direction - 1) % 4
            else:
                direction = (direction + 1) % 4
    
    return time

def main():
    N = int(input().strip())
    K = int(input().strip())
    apples = []
    for _ in range(K):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        apples.append((x, y))
    L = int(input().strip())
    
    directions = [list(input().split()) for _ in range(L)]
    directions = [(int(t), d) for t, d in directions]

    print(count_game_over_time(N, apples, directions))

if __name__ == '__main__':
    main()