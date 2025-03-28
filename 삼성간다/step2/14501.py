# 백준 14501. 퇴사
# https://www.acmicpc.net/problem/14501
import sys
def dfs(day, curr_profit):
    global max_profit, N, schedules

    if day > N:
        max_profit = max(max_profit, curr_profit)
        return
    
    dfs(day + 1, curr_profit)

    if day + schedules[day][0] - 1 <= N:
        dfs(day + schedules[day][0], curr_profit + schedules[day][1])

def main():
    global max_profit, N, schedules
    N = int(sys.stdin.readline().strip())
    schedules = [None] +[tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

    max_profit = 0

    dfs(day=1, curr_profit=0)

    print(max_profit)

if __name__ == '__main__':
    main()