# 백준 14891. 톱니바퀴
# https://www.acmicpc.net/problem/14891

# 톱니바퀴의 초기 상태와 톱니바퀴를 회전시킨 방법이 주어졌을 때, 최종 톱니바퀴의 상태를 구하는 프로그램 작성
from collections import deque
def rotate(gear, direction):
    gear.rotate(direction)

def process_gear(gears, gear_idx, direction):
    directions = [0] * 4
    directions[gear_idx] = direction

    for i in range(gear_idx, 0, -1):
        if gears[i][6] != gears[i - 1][2]:
            directions[i - 1] = -directions[i]
        else:
            break
    
    for i in range(gear_idx, 3):
        if gears[i][2] != gears[i + 1][6]:
            directions[i + 1] = -directions[i]
        else:
            break

    for i in range(4):
        if directions[i] != 0:
            rotate(gears[i], directions[i])

def calculate_gears(gears):
    scores_table = [1, 2, 4, 8]
    scores = 0

    for i in range(4):
        if gears[i][0] == 1:
            scores += scores_table[i]
    
    return scores

def main():
    gears = [deque(map(int, input().strip())) for _ in range(4)]
    K = int(input().strip())

    for _ in range(K):
        gear_num, direction = map(int, input().split())
        process_gear(gears, gear_num - 1, direction)
    
    print(calculate_gears(gears))

if __name__ == '__main__':
    main()