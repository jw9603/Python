# 백준 14499. 주사위 굴리기
# https://www.acmicpc.net/problem/14499
# 백준 14499. 주사위 굴리기
# https://www.acmicpc.net/problem/14499
def print_dice_result(commands, dice, x, y):
    global n, m, board

    # 동, 서, 북, 남
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for command in commands:
        d = command - 1

        next_x, next_y = x + dx[d], y + dy[d]

        if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
            continue
        
        dice = roll_dice(dice, command)

        x, y = next_x, next_y

        if board[x][y] == 0:
            board[x][y] = dice[1]
        else:
            dice[1] = board[x][y]
            board[x][y] = 0
        
        print(dice[0])


def roll_dice(dice, command):
    top, bottom, north, south, west, east = dice

    if command == 1:   # 동
        return [west, east, north, south, bottom, top]
    elif command == 2: # 서
        return [east, west, north, south, top, bottom]
    elif command == 3: # 북
        return [south, north, top, bottom, west, east]
    else:              # 남
        return [north, south, bottom, top, west, east]
        

def main():
    global n, m, board
    n, m, x, y, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    commands = list(map(int, input().split()))

    dice = [0] * 6

    print_dice_result(commands, dice, x, y)

if __name__ == '__main__':
    main()
