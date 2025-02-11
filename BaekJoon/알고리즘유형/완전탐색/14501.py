# 백준 14501. 퇴사
# https://www.acmicpc.net/problem/14501
import sys
N = int(sys.stdin.readline().strip())
schedules = [None] + [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

max_profit = 0

def sol(day, profit):
    global max_profit
    
    if day > N:
        max_profit = max(max_profit, profit)
        return

    sol(day + 1, profit)
    
    if day + schedules[day][0] - 1 <= N:
        sol(day + schedules[day][0], profit + schedules[day][1])

sol(1, 0)
print(max_profit)
    