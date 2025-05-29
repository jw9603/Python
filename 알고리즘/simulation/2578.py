# 백준 2578. 빙고
# https://www.acmicpc.net/problem/2578
############################# 문제 이해 #############################
# 빙고판의 수는 1부터 25
# 선 세 개 이상 그어지는 순간 빙고라고 외친다. 가장 먼저 외치는 사람이 게임의 승자.
# 철수는 친구들과 빙고 게임을 하고 있다.
# 철수가 빙고판에 쓴 수들과 사회자가 부르는 수의 순서가 주어질 때,
# 사회자가 몇 번째 수를 부른 후 철수가 '빙고'를 외치게 되는지를 출력하는 프로그램을 작성.
############################# 문제 이해 #############################
def check_bingo(bingo):
    cnt = 0

    # 가로
    for row in bingo:
        if row.count(0) == 5:
            cnt += 1
    
    # 세로
    for col in range(5):
        num = 0
        for row in range(5):
            if bingo[row][col] == 0:
                num += 1
        if num == 5:
            cnt += 1
    
    # 오른쪽 대각선
    num = 0
    for i in range(5):
        if bingo[i][4 - i] == 0:
            num += 1
    if num == 5:
        cnt += 1
    
    # 왼쪽 대각선
    num = 0
    for i in range(5):
        if bingo[i][i] == 0:
            num += 1
    if num == 5:
        cnt += 1

    return cnt

def sol(bingo, nums):
    cnt = 0

    for i in range(25):
        for j in range(5):
            for k in range(5):
                if nums[i] == bingo[j][k]:
                    bingo[j][k] = 0
                    cnt += 1
        if cnt >= 12 and check_bingo(bingo) >= 3:
            
            return cnt
            
def main():
    bingo = [list(map(int, input().split())) for _ in range(5)]
    nums = []

    for _ in range(5):
        nums.extend(list(map(int, input().split())))

    print(sol(bingo, nums))

if __name__ == '__main__':
    main()