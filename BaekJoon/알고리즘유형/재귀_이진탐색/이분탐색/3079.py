# 백준 3079. 입국 심사
# https://www.acmicpc.net/problem/3079

import sys
N, M = map(int, sys.stdin.readline().split())
times = [int(sys.stdin.readline().strip()) for _ in range(N)]

def sol(N, M, times):
    low, high = 1, max(times) * M
    result = 0
    while low <= high:
        mid = (low + high) // 2
        total_people = sum(mid // time for time in times)

        if total_people >= M:
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result
print(sol(N=N, M=M, times=times))