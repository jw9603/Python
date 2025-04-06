# 백준 17825. 주사위 윷놀이
# https://www.acmicpc.net/problem/17825

# 처음에는 시작 칸에 말 4개가 있다.
# 말은 게임판에 그려진 화살표의 방향대로만 이동할 수 있다.

# 게임은 10개의 턴으로 이루어진다.
# 매 턴마다 1부터 5까지 한 면에 하나씩 적혀있는 5면체 주사위를 굴리고,
# 도착 칸에 있지 않은 말을 하나 골라 주사위에 나온 수 만큼 이동시킨다.
# 말이 이동을 마치는 칸에 다른 말이 있으면 그 말은 고를 수 없다.
# 단, 이동을 마치는 칸이 도착 칸이면 고를 수 있다.
# 말이 이동을 마칠 때마다 칸에 적혀있는 수가 점수에 추가된다.
# 말이 이동을 마칠 때마다 칸에 적혀있는 수가 점수에 추가된다.

def create_move_graph():
    
    move = {} # i번 칸에서 주사위 수에 따라 이동할 수 있는 도착 위치 리스트
    # 칸 i에서 주사위 x가 나왔을 때 도착 위치 = move[i][x]

    for i in range(17):
        if i in [5, 10, 15]:
            continue
        move[i] = [0, i + 1, i + 2, i + 3, i + 4, i + 5]
    move[16][5] = 32

    move[17] = [0, 18, 19, 20, 32, 32] # 34
    move[18] = [0, 19, 20, 32, 32, 32] # 36
    move[19] = [0, 20, 32, 32, 32, 32] 
    move[20] = [0, 32, 32, 32, 32, 32]

    move[5] = [0, 21, 22, 23, 29, 30]
    move[10] = [0, 24, 25, 29, 30, 31]
    move[15] = [0, 26, 27, 28, 29, 30]

    move[21] = [0, 22, 23, 29, 30, 31]
    move[22] = [0, 23, 29, 30, 31, 20]
    move[23] = [0, 29, 30, 31, 20, 32]
    move[24] = [0, 25, 29, 30, 31, 20]
    move[25] = [0, 29, 30, 31, 20, 32]
    move[26] = [0, 27, 28, 29, 30, 31]
    move[27] = [0, 28, 29, 30, 31, 20]
    move[28] = [0, 29, 30, 31, 20, 32]
    move[29] = [0, 30, 31, 20, 32, 32]
    move[30] = [0, 31, 20, 32, 32, 32]
    move[31] = [0, 20, 32, 32, 32, 32]

    return move

def sol(dice):
    graph = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40,
             13, 16, 19,  # index 21 ,22, 23
             22, 24,      # index 24, 25
             28, 27, 26,  # index 26, 27, 28
             25, 30, 35 , 0] # index 29, 30, 31, 32

    move = create_move_graph()
    max_val = 0
    def dfs(turn, index, horse_list, cnt):
        '''
        turn: 몇 번째 턴인지
        index: 각 턴마다의 주사위 위치

        '''
        nonlocal max_val
        if turn == 10:
            max_val = max(max_val, cnt)
            return
        for i in range(4): # i는 4개의 말
            if horse_list[i] == 32:
                continue
            j = move[horse_list[i]][dice[index]] # 현재 말 i를 주사위 수만큼 이동

            if j not in horse_list or j == 32:
                dfs(turn + 1, index + 1, horse_list[:i] + [j] + horse_list[i + 1:], cnt + graph[j])
    dfs(0, 0, [0, 0, 0, 0], 0)
    return max_val

def main():
    dice = list(map(int, input().split()))
    print(sol(dice))

if __name__ == '__main__':
    main()