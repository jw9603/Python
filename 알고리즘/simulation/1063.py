# 백준 1063. 킹
# https://www.acmicpc.net/problem/1063
############################### 문제 이해 ###############################
# 8*8 크의 체스판, 왕이 하나 있다. 왕의 현재 위치 주어진다.
# 체스판에는 돌이 하나 있는데, 돌과 같은 곳으로 이동할 때는, 돌을 킹이 움직인 방향과
# 같은 방향으로 한 칸 이동시킨다.
# 입력으로 킹이 어떻게 움직여야 하는지 주어진다.
# 입력으로 주어진 대로 움직여서 킹이나 돌이 체스판 밖으로 나갈 경우에는 그 이동은 건너 뛰고
# 다음 이동을 한다.
# 킹과 돌의 마지막 위치를 구해라

# 입력
# 첫째 줄에 킹의 위치, 돌의 위치, 움직이는 횟수 N이 주어진다.
# 둘째 줄부터 N개의 줄에는 킹이 어떻게 움직여야 하는지 주어진다.
############################### 문제 이해 ###############################
def sol(N, king, stone):
    directions = {'R' : [1, 0], 'L' : [-1, 0], 'B': [0, -1], 'T' : [0, 1], 'RT' : [1, 1], 'LT' : [-1, 1], 'RB' : [1, -1], 'LB' : [-1, -1]}
    
    for _ in range(int(N)):
        move = input().strip()

        next_x, next_y = king[0] + directions[move][0], king[1] + directions[move][1]
        
        if 0 < next_x <= 8 and 0 < next_y <= 8:
            # 돌이랑 킹이 겹칠 경우
            if next_x == stone[0] and next_y == stone[1]:
                stone_x = stone[0] + directions[move][0]
                stone_y = stone[1] + directions[move][1]

                if 0 < stone_x <= 8 and 0 < stone_y <= 8:
                    king = [next_x, next_y]
                    stone = [stone_x, stone_y]
            # 안겹칠 경우
            else:
                king = [next_x, next_y]
    
    return f"{chr(king[0] + 64)}{king[1]}", f"{chr(stone[0] + 64)}{stone[1]}"

def main():
    king, stone, N = input().split()
    king = list(map(int, [ord(king[0]) - 64, king[1]]))
    stone = list(map(int, [ord(stone[0]) - 64, stone[1]]))
    # print(king) # [1, 1]
    # print(stone) # [1, 2]

    print(*sol(N, king, stone), sep='\n')

if __name__ == '__main__':
    main()