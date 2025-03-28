# 백준 14499. 주사위 굴리기
# https://www.acmicpc.net/problem/14499
import sys
def roll_dice(dice, direction):
   top, bottom, north, south, west, east = dice

   if direction == 1: # 동
      return [west, east, north, south, bottom, top]
   elif direction == 2: # 서
       return [east, west, north, south, top, bottom]
   elif direction == 3: # 북
       return [south, north, top, bottom, west, east]
   elif direction == 4:
       return [north, south, bottom, top, west, east]

def main():

    N, M, x, y, K = map(int, sys.stdin.readline().split())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    commands = list(map(int, sys.stdin.readline().split()))

    # 동, 서, 북, 남
    dx = [0, 0, -1, 1] 
    dy = [1, -1, 0, 0]

    dice = [0] * 6

    for command in commands:
        direction = command - 1
        next_x, next_y = x + dx[direction], y + dy[direction]

        if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M:
            continue
        
        x, y = next_x, next_y

        dice = roll_dice(dice, command)

        # 이동한 칸에 쓰여있는 수가 0이면, 주사위 바닥면에 쓰여있는 수가 칸에 복사된다.
        if board[x][y] == 0:
            board[x][y] = dice[1]
        else:
        # 0이 아니면, 칸에 쓰여있는 수가 주사위의 바닥면에 복사되고 칸에 쓰여있는 수가 0이 된다.
            dice[1] = board[x][y]
            board[x][y] = 0
        
        print(dice[0])

if __name__ == '__main__':
    main()